# Telegram voice/STT plan for OpenClaw

Status: discovery only, no implementation yet  
Date: 2026-04-26

## Goal

Telegram voice message -> transcript -> normal OpenClaw reasoning -> text reply in the same Telegram session.

## Discovery summary

### 1) Telegram channel: does it support voice/audio?

Yes, in the packaged OpenClaw codebase.

Evidence found in local installation:
- Telegram config exposes `disableAudioPreflight` with comment: "skip automatic voice-note transcription" for groups/topics.
- Telegram media runtime re-exports `transcribeFirstAudio(...)`.
- Shared media runtime has `transcribeFirstAudio` specifically documented as running **before mention checking**, so voice notes can be processed in Telegram groups.
- Changelog entries mention:
  - DM voice-note preflight transcription restored;
  - Telegram voice-note `.ogg` is transcoded before local whisper fallback;
  - audio download/transcription handling for Telegram was fixed multiple times.

Conclusion:
- inbound Telegram `voice` / `audio` attachments are supported by the channel design;
- the intended path is: Telegram attachment -> audio preflight transcription / media understanding -> transcript -> agent turn.

### 2) Built-in STT/transcription in OpenClaw

Yes.

OpenClaw has built-in media/STT runtime:
- `transcribeAudioFile(...)`
- `transcribeFirstAudio(...)`
- `tools.media.audio.*` config
- provider-based and CLI-based transcription models
- optional transcript echo: `tools.media.audio.echoTranscript`

There is also a deprecated legacy path:
- `messages.audio.transcription.command`

Preferred modern path:
- `tools.media.audio.models`

### 3) STT providers/models available in this installed OpenClaw package

Built-in API providers discovered in local package:
- `openai` -> default audio model `gpt-4o-transcribe`
- `groq` -> default audio model `whisper-large-v3-turbo`
- `deepgram` -> default audio model `nova-3`
- `elevenlabs` -> default audio model `scribe_v2`
- `mistral` -> default audio model `voxtral-mini-latest`
- `xai` -> default audio model `grok-stt`

Built-in local/CLI path discovered in runtime:
- `whisper-cli` (whisper.cpp style)
- `whisper`
- `parakeet-mlx`
- `sherpa-onnx-offline`

Important current-state finding on this VPS/session:
- `openclaw infer audio providers --json` returned `[]`
- relevant API keys are currently unset in the visible env/template/backup files
- local STT binaries are currently absent: `whisper-cli`, `whisper`, `ffmpeg`, `ffprobe`, `parakeet-mlx`, `sherpa-onnx-offline`
- `openclaw status` currently shows plugin runtime init problems in this shell environment (read-only plugin-runtime-deps path), so live verification from CLI is incomplete

Implication:
- the code supports STT, but this host is **not currently configured** for a working STT provider.

## Options

### Option A — API-based STT inside OpenClaw (recommended default)

Use native OpenClaw media transcription with `tools.media.audio.models` and one API provider.

Recommended first implementation:
- primary: `openai / gpt-4o-transcribe`
- optional fallback later: `groq / whisper-large-v3-turbo`

Why this is the default:
- simplest path with least custom code
- best fit for your stated preference
- no heavy local inference
- failure handling can stay inside OpenClaw reply flow
- easy rollback to plain text-only Telegram

Complexity:
- low

Price:
- OpenAI `gpt-4o-transcribe`: about **$0.006/min**
- lower-cost alternatives already supported by OpenClaw:
  - Groq `whisper-large-v3-turbo`: **$0.04/hour**
  - xAI `grok-stt` batch: **$0.10/hour**
  - Deepgram `nova-3`: **$0.0077/min**
  - Mistral realtime transcription family pricing seen around **$0.006/min**

VPS load:
- low
- mostly network + short file handling

Reliability:
- high if provider key is configured and retries/errors are surfaced cleanly
- OpenAI is the safest default; Groq is attractive as a cheap fallback

Privacy:
- medium
- audio leaves VPS and goes to external API provider
- can be acceptable if secrets are handled correctly and logs avoid payload leakage

Rollback:
- remove/disable `tools.media.audio` config
- optionally disable Telegram audio preflight / related routing
- bot returns to text-only Telegram behavior

### Option B — local `whisper.cpp` via CLI model

Use OpenClaw CLI-based media model with `whisper-cli`.

Expected shape:
- install `whisper-cli`
- install `ffmpeg` / `ffprobe`
- configure `tools.media.audio.models` with `type: cli`
- let OpenClaw transcode Telegram `.ogg` to `.wav` when needed

Complexity:
- medium

Price:
- near-zero API cost
- real cost is CPU/RAM/time on VPS

VPS load:
- medium to high depending on model and message volume
- likely the heaviest option here

Reliability:
- medium
- fewer external dependencies, but more operational sharp edges:
  - binary install
  - model file management
  - CPU spikes
  - slower inference
  - ffmpeg dependency

Privacy:
- high
- audio stays on your infrastructure

Rollback:
- remove CLI model config
- uninstall binaries later if desired
- revert to API provider or text-only mode

### Option C — intermediate webhook / microservice

Put a small STT service between Telegram/OpenClaw and the chosen transcription engine.

Two realistic sub-forms:
1. webhook service that accepts audio and returns transcript
2. OpenAI-compatible transcription endpoint wrapper so OpenClaw calls it like a provider

Use this if we need:
- custom retry logic
- queueing / rate limiting
- transcript normalization
- provider abstraction
- central audit / redaction / metrics
- reuse by multiple bots/channels later

Complexity:
- medium-high

Price:
- service maintenance cost + underlying STT provider cost
- cheapest if backed by Groq or local whisper; simplest if backed by OpenAI

VPS load:
- low to medium for API-backed service
- medium to high for locally-hosted whisper-backed service

Reliability:
- medium
- more moving parts than Option A
- can become high only if we intentionally invest in retries/queueing/observability

Privacy:
- varies
- high if local backend
- medium if wrapper forwards audio to external API

Rollback:
- detach OpenClaw from service endpoint
- point back to direct provider config or disable STT entirely

## Recommendation

### Default recommendation

Implement **Option A: native OpenClaw API-based STT**, starting with:
- provider: `openai`
- model: `gpt-4o-transcribe`

### Alternative if cost matters more than default-vendor conservatism

Use:
- provider: `groq`
- model: `whisper-large-v3-turbo`

### Why not local whisper first

Because today on this VPS:
- no local whisper binary
- no ffmpeg/ffprobe
- more operational work
- higher CPU burden
- not aligned with your “simple and reliable first” preference

## Proposed future implementation phases

### Phase 1 — enable the simplest working STT path

- confirm active Telegram bot/channel config location
- configure `tools.media.audio.enabled`
- configure `tools.media.audio.models` with API provider/model
- set safe limits: timeout, max bytes, optional language hint
- verify transcript becomes normal message text for the agent
- ensure errors are returned as readable Telegram replies

### Phase 2 — hardening

- add clean user-facing STT failure message
- ensure secrets are only read from env/secret storage
- ensure transcript/audio payloads are not written to normal logs
- verify Dashboard session visibility for Telegram-origin session
- add optional provider fallback if desired

### Phase 3 — optional improvements

- optional `echoTranscript` for debugging only (likely off in production)
- optional cost-optimized fallback provider
- optional per-chat/group policy controls
- optional webhook abstraction if we later need multi-bot reuse or provider switching

## Implementation notes to preserve in the future task

### Config direction

Prefer modern config path:
- `tools.media.audio.*`

Avoid building on deprecated path unless required:
- `messages.audio.transcription.command`

### Error handling requirement

If STT fails, the user should get a human-readable Telegram reply, for example:
- “Не смог расшифровать голосовое сообщение. Попробуй ещё раз или пришли текст.”

### Logging/security requirement

Must ensure:
- API keys are not printed in logs
- raw Authorization headers are not logged
- transcript logging is minimized or disabled where possible
- full audio blobs/base64 are not persisted in chat logs unless explicitly required

### Dashboard requirement

Need to verify that Telegram-origin message still creates/uses a normal OpenClaw session visible in Dashboard after transcription path is enabled.

## Future DoD

- Telegram voice becomes text inside OpenClaw processing path
- OpenClaw replies to the *content* of the voice message
- if STT fails, user gets a clear readable error
- session is visible in Dashboard
- secrets are not logged

## Recommended implementation decision

Proceed with:
- **Option A / OpenAI `gpt-4o-transcribe` first**
- optional cheap fallback later: **Groq `whisper-large-v3-turbo`**
- do **not** start with local Whisper on this VPS
- do **not** start with webhook service unless direct provider config proves insufficient

## Notes from current discovery

Current blockers before implementation:
- no STT provider key configured
- no local STT binaries installed
- CLI environment currently shows plugin init issues, so after config we should validate in the real gateway runtime, not rely only on this shell
