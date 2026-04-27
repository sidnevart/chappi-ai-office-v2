#!/usr/bin/env bash
set -euo pipefail
TS="$(date +%Y%m%d-%H%M%S)"
CONFIG_TOKEN="$(python3 - <<'PY'
import json
print(json.load(open('/root/.openclaw/openclaw.json'))['gateway']['auth']['token'])
PY
)"
mkdir -p /root/.openclaw/fix-backups
cp -a /etc/systemd/system/openclaw-gateway.service "/root/.openclaw/fix-backups/openclaw-gateway.service.${TS}.bak"
cp -a /root/.config/systemd/user/openclaw-gateway.service "/root/.openclaw/fix-backups/openclaw-gateway.user.service.${TS}.bak" 2>/dev/null || true
cp -a /etc/openclaw/gateway.env "/root/.openclaw/fix-backups/gateway.env.${TS}.bak"
python3 - <<'PY'
from pathlib import Path
p = Path('/etc/systemd/system/openclaw-gateway.service')
text = p.read_text()
old = 'ExecStart=/usr/bin/openclaw gateway run --bind loopback --port 18789 --auth none\n'
new = 'ExecStart=/usr/bin/openclaw gateway run --bind loopback --port 18789\n'
if old in text:
    text = text.replace(old, new)
p.write_text(text)
PY
cat > /etc/openclaw/gateway.env <<EOF
OPENCLAW_GATEWAY_TOKEN=${CONFIG_TOKEN}
OPENCLAW_STATE_DIR=/root/.openclaw
OPENCLAW_CONFIG_PATH=/root/.openclaw/openclaw.json
OPENCLAW_DISABLE_BONJOUR=1
EOF
chmod 600 /etc/openclaw/gateway.env
systemctl --user disable --now openclaw-gateway.service || true
systemctl daemon-reload
systemctl reset-failed openclaw-gateway.service || true
systemctl restart openclaw-gateway.service
systemctl restart openclaw-office.service
sleep 8
{
  echo '=== ps ==='
  ps -ef | grep -i '[o]penclaw-gateway'
  echo '=== system status ==='
  systemctl status openclaw-gateway.service --no-pager -l | sed -n '1,80p'
  echo '=== user status ==='
  systemctl --user status openclaw-gateway.service --no-pager -l 2>/dev/null | sed -n '1,40p' || true
  echo '=== office status ==='
  systemctl status openclaw-office.service --no-pager -l | sed -n '1,60p'
  echo '=== exporter ==='
  python3 /opt/openclaw-monitoring/scripts/openclaw_usage_exporter.py
  grep -E 'openclaw_exporter_success|openclaw_gateway_duplicate_supervisor_recent|openclaw_gateway_system_service_active|openclaw_gateway_user_service_active' /var/lib/node_exporter/textfile_collector/openclaw.prom
} > /root/.openclaw/fix-backups/gateway-fix-result.${TS}.log 2>&1
