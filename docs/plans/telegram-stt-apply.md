# Apply notes for Telegram voice/STT

Target live config discovered on this VPS:
- `/root/.openclaw/openclaw.json`

Required secret before this can work:
- `OPENAI_API_KEY` in the gateway service environment

Minimal live change set:
1. Add `OPENAI_API_KEY` to the gateway service environment.
2. Merge `telegram-stt-config-snippet.jsonc` into `/root/.openclaw/openclaw.json` under `tools`.
3. Restart the OpenClaw gateway service.
4. Verify:
   - `openclaw infer audio providers --json` should include `openai`
   - send a Telegram voice message to the bot

Recommended verification cases:
- short Russian voice note
- long voice note (~20-40 sec)
- broken provider / invalid key -> readable Telegram error

Current blockers in this sandbox:
- cannot write live files outside `/opt/openclaw-stack/workspace`
- no STT API key is configured yet
