# Monitoring plan for OpenClaw host

## Goal
Поднять минимальный и надёжный monitoring stack для одного Ubuntu 24.04 VPS с OpenClaw, не ломая nginx / docker / openclaw / ollama / claude / codex / Telegram / Composio.

## Read-only audit summary

### Host / services
- OS/runtime: Ubuntu 24.04 VPS
- Docker Compose available: `v5.1.3`
- `docker ps`:
  - `searxng/searxng` published on `:8888`
- `systemctl status nginx`: active/running
- `systemctl status openclaw-gateway`: active/running, recently restarted
- `openclaw gateway health`: `OK`, Telegram healthy
- `openclaw gateway probe`: local gateway `ws://127.0.0.1:18789` reachable, admin-capable
- `openclaw tasks list`: available, currently 0 tasks
- `openclaw gateway usage-cost`: available, shows 30-day aggregate usage/cost

### Listening ports right now
- `127.0.0.1:18789` — OpenClaw Gateway
- `127.0.0.1:18791` — OpenClaw browser server
- `127.0.0.1:5180` — OpenClaw Office UI
- `127.0.0.1:11434` — Ollama
- `0.0.0.0:80`, `:8081`, `:8443` — nginx
- `0.0.0.0:8888` — Searxng container
- `0.0.0.0:22` — SSH

### Capacity snapshot
- Disk: `/` = `79G`, used `17G`, free `59G` (~22%)
- RAM: `7.7Gi`, used `2.8Gi`, available `4.9Gi`
- Swap: `3.8Gi`, used `39Mi`

### Notable observations / risks before rollout
1. `openclaw gateway usage-cost` is available, so usage exporter can rely on CLI at least partially.
2. `openclaw tasks list` is available, so task counters are extractable.
3. There is no current sign of Grafana/Prometheus/node-exporter/cadvisor already occupying common monitoring ports.
4. `openclaw-gateway.service` logs show a recent restart and mention `auth mode=none explicitly configured`; that is not part of this task, but monitoring rollout should avoid touching gateway auth.
5. nginx is already a shared reverse proxy, so `/grafana` must be added surgically.

## Proposed architecture

### Components
Use one Docker Compose stack under `/opt/openclaw-monitoring`:
1. **Prometheus**
2. **Grafana**
3. **node-exporter**
4. **cadvisor** *(conditional but recommended; include only if it starts cleanly and does not create host friction)*

Host-side helper:
5. **OpenClaw usage exporter script** writing Prometheus textfile metrics for node-exporter.

No extra long-lived custom app daemon unless necessary.

## Port plan
Internal/local only:
- Grafana: `127.0.0.1:3300` *(chosen to avoid common collisions with 3000)*
- Prometheus: `127.0.0.1:9090`
- node-exporter: `127.0.0.1:9100`
- cadvisor: `127.0.0.1:8083` *(only if enabled)*

Public exposure:
- **Only nginx route `/grafana/`**
- Prometheus remains local-only
- node-exporter remains local-only
- cadvisor remains local-only

## Files to create
Under `/opt/openclaw-monitoring/`:
- `docker-compose.yml`
- `prometheus/prometheus.yml`
- `prometheus/rules/` *(optional initially; can stay empty)*
- `grafana/provisioning/datasources/prometheus.yml`
- `grafana/provisioning/dashboards/dashboards.yml`
- `grafana/dashboards/server-overview.json`
- `grafana/dashboards/openclaw-usage-overview.json`
- `scripts/openclaw_usage_exporter.py` *(or `.sh` if Python version is too trivial)*
- `README.md`

Host metric directory:
- `/var/lib/node_exporter/textfile_collector/openclaw.prom`

Scheduling / refresh:
- preferred: one lightweight cron entry in `/etc/cron.d/openclaw-monitoring`
  - updates textfile metrics every minute
  - avoids adding another systemd service+timer pair

Potential nginx change:
- existing active nginx vhost file (likely `/etc/nginx/conf.d/00-default.conf`) gets one extra location block for `/grafana/`

## Reverse proxy design
- nginx `location /grafana/` → local Grafana on `127.0.0.1:3300`
- proxy headers preserved
- websocket headers included
- if Grafana needs subpath mode, set:
  - `GF_SERVER_ROOT_URL=%(protocol)s://%(domain)s/grafana/`
  - `GF_SERVER_SERVE_FROM_SUB_PATH=true`
- Grafana auth stays enabled with explicit admin login/password
- no direct external publish for Prometheus

## Exporter design
The OpenClaw exporter should:
- run locally on host
- call read-only commands where available:
  - `openclaw gateway health`
  - `openclaw gateway probe`
  - `openclaw tasks list`
  - `openclaw gateway usage-cost`
- emit Prometheus textfile metrics like:
  - `openclaw_gateway_health_ok`
  - `openclaw_gateway_probe_ok`
  - `openclaw_tasks_total`
  - `openclaw_usage_cost_usd_30d`
  - `openclaw_usage_tokens_30d`
  - `openclaw_usage_command_available`
- degrade gracefully if a CLI command is missing or output changes
- never print or store secrets in metrics/logs

Important limitation:
- detailed counters like sessions/tasks/model usage/cost/tokens/fallbacks are only available to the extent OpenClaw CLI/logs expose them without unstable parsing.
- initial version should prefer stable health/status/cost/task metrics over brittle deep parsing.

## Dashboard plan
### 1) Server Overview
Panels:
- CPU usage
- RAM usage
- disk usage / inode trend if available
- swap usage
- network in/out
- load average
- uptime
- Docker container up/down state
- optionally container CPU/memory via cadvisor

### 2) OpenClaw Usage Overview
Panels:
- gateway health
- gateway reachable/admin-capable flags
- task count / task pressure if extractable
- 30-day usage cost
- 30-day token count
- command availability flags
- exporter last successful scrape timestamp

## Rollback plan
1. stop and remove monitoring compose stack:
   - `docker compose -f /opt/openclaw-monitoring/docker-compose.yml down`
2. remove nginx `/grafana` location and reload nginx
3. remove `/etc/cron.d/openclaw-monitoring`
4. optionally remove `/opt/openclaw-monitoring`
5. optionally remove `/var/lib/node_exporter/textfile_collector/openclaw.prom`

Rollback should not affect Gateway, Telegram, Composio, Office UI, Searxng, or model settings.

## Risks
1. **Subpath Grafana** can be misconfigured if `/grafana/` and root URL disagree.
2. **cadvisor** adds extra visibility but also extra mounts; if it behaves oddly, skip it.
3. **CLI parsing fragility** for OpenClaw usage metrics; exporter should fail soft.
4. **Resource overhead** is modest but non-zero; expected acceptable on current free RAM/disk.
5. **Nginx collision risk** if current config already has hidden subpath assumptions; mitigate with surgical backup + `nginx -t`.

## Implementation order after confirmation
1. Create `/opt/openclaw-monitoring` structure
2. Write Compose, Prometheus, Grafana provisioning, dashboards
3. Write local OpenClaw exporter script
4. Add one cron entry for textfile refresh
5. Add nginx `/grafana/` location
6. `nginx -t` and reload
7. Start compose stack
8. Verify local curl / compose / scrape / Grafana route / gateway health

## What will NOT be touched
- OpenClaw model fallback/settings
- Telegram
- Composio
- existing Gateway bind/port
- existing Searxng container
- direct public exposure of Prometheus
