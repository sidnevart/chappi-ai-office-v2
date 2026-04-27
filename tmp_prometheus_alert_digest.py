#!/usr/bin/env python3
import json
import sys
import urllib.request
from pathlib import Path

STATE_PATH = Path('/opt/openclaw-monitoring/state/alert_state.json')
ALERTS_URL = 'http://127.0.0.1:9090/api/v1/alerts'


def fetch_alerts():
    with urllib.request.urlopen(ALERTS_URL, timeout=10) as resp:
        data = json.load(resp)
    groups = data.get('data', {}).get('alerts', [])
    alerts = []
    for item in groups:
        state = (item.get('state') or '').lower()
        if state not in {'firing', 'pending'}:
            continue
        labels = item.get('labels') or {}
        annotations = item.get('annotations') or {}
        alerts.append({
            'name': labels.get('alertname', 'unknown'),
            'severity': labels.get('severity', 'unknown'),
            'state': state,
            'summary': annotations.get('summary', labels.get('alertname', 'unknown alert')),
            'description': annotations.get('description', ''),
        })
    alerts.sort(key=lambda x: (x['severity'], x['name']))
    return alerts


def key(alert):
    return f"{alert['name']}|{alert['severity']}|{alert['state']}"


def load_previous():
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {}


def save_current(alerts):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps({'alerts': alerts}, ensure_ascii=False, indent=2))


def main():
    try:
        current = fetch_alerts()
    except Exception as e:
        print('ALERT: не удалось прочитать Prometheus alerts API:', str(e))
        return 0

    previous = load_previous().get('alerts', [])
    prev_map = {key(a): a for a in previous}
    curr_map = {key(a): a for a in current}

    new_alerts = [curr_map[k] for k in curr_map.keys() - prev_map.keys()]
    resolved = [prev_map[k] for k in prev_map.keys() - curr_map.keys()]

    save_current(current)

    if not new_alerts and not resolved:
        print('NO_ALERT_CHANGES')
        return 0

    lines = []
    if new_alerts:
        lines.append('Новые алерты:')
        for alert in new_alerts:
            lines.append(f"- [{alert['severity']}/{alert['state']}] {alert['summary']}")
            if alert['description']:
                lines.append(f"  {alert['description']}")
    if resolved:
        if lines:
            lines.append('')
        lines.append('Снялись алерты:')
        for alert in resolved:
            lines.append(f"- [{alert['severity']}] {alert['summary']}")
    print('\n'.join(lines))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
