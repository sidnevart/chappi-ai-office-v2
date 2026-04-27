#!/usr/bin/env python3
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

OUT = Path('/var/lib/node_exporter/textfile_collector/openclaw.prom')
TIMEOUT = 25

ANSI_RE = re.compile(r'\x1b\[[0-9;?]*[A-Za-z]')
EMITTED_META = set()


def sanitize(text: str) -> str:
    text = ANSI_RE.sub('', text or '')
    return text.replace('\r', '')


def run(cmd):
    try:
        env = os.environ.copy()
        env.setdefault('TERM', 'dumb')
        env.setdefault('NO_COLOR', '1')
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=TIMEOUT,
            check=False,
            env=env,
        )
        return proc.returncode, sanitize(proc.stdout).strip()
    except FileNotFoundError:
        return 127, ''
    except subprocess.TimeoutExpired as e:
        return 124, (e.stdout or '').strip() if isinstance(e.stdout, str) else ''


def run_shell(command: str):
    return run(['bash', '-lc', command])


def metric_lines(name, value, help_text, metric_type='gauge', labels=None):
    lines = []
    if help_text is not None and name not in EMITTED_META:
        lines.append(f'# HELP {name} {help_text}')
        lines.append(f'# TYPE {name} {metric_type}')
        EMITTED_META.add(name)
    if labels:
        label_text = ','.join(f'{k}="{str(v).replace(chr(34), chr(92)+chr(34))}"' for k, v in sorted(labels.items()))
        lines.append(f'{name}{{{label_text}}} {value}')
    else:
        lines.append(f'{name} {value}')
    return lines


def parse_shorthand_number(raw: str) -> float:
    s = raw.strip().lower().replace(',', '')
    mult = 1.0
    if s.endswith('k'):
        mult = 1_000.0
        s = s[:-1]
    elif s.endswith('m'):
        mult = 1_000_000.0
        s = s[:-1]
    elif s.endswith('b'):
        mult = 1_000_000_000.0
        s = s[:-1]
    return float(s) * mult


def bool_metric(ok: bool) -> int:
    return 1 if ok else 0


def parse_gateway_health(text: str):
    ok = 'Gateway Health' in text and re.search(r'\bOK\b', text) is not None
    telegram_ok = re.search(r'Telegram:\s+ok', text, re.I) is not None
    return ok, telegram_ok


def parse_gateway_probe(text: str):
    reachable = re.search(r'Reachable:\s+yes', text, re.I) is not None or re.search(r'Connect:\s+ok', text, re.I) is not None
    admin = re.search(r'Capability:\s+admin-capable', text, re.I) is not None
    return reachable, admin


def parse_tasks(text: str):
    if not text:
        return 0
    m = re.search(r'Background tasks:\s*(\d+)', text)
    if m:
        return int(m.group(1))
    if 'No background tasks found' in text:
        return 0
    return 0


def parse_status(text: str):
    sessions = 0
    agents = 0
    for line in text.splitlines():
        if '│' not in line:
            continue
        parts = [p.strip() for p in line.split('│') if p.strip()]
        if len(parts) < 2:
            continue
        key, value = parts[0], parts[1]
        if key.lower() == 'sessions':
            m = re.search(r'(\d+)\s+active', value, re.I)
            if m:
                sessions = int(m.group(1))
        elif key.lower() == 'agents':
            m = re.match(r'(\d+)', value)
            if m:
                agents = int(m.group(1))
            if not sessions:
                m = re.search(r'sessions\s+(\d+)', value, re.I)
                if m:
                    sessions = int(m.group(1))
    return sessions, agents


def parse_usage(text: str):
    total_cost = 0.0
    total_tokens = 0.0
    latest_cost = 0.0
    latest_tokens = 0.0

    m = re.search(r'Total:\s*\$([0-9]+(?:\.[0-9]+)?)\s*·\s*([0-9.,]+[kmb]?)\s+tokens', text, re.I)
    if m:
        total_cost = float(m.group(1))
        total_tokens = parse_shorthand_number(m.group(2))

    m = re.search(r'Latest day:\s*([^·]+)·\s*\$([0-9]+(?:\.[0-9]+)?)\s*·\s*([0-9.,]+[kmb]?)\s+tokens', text, re.I)
    if m:
        latest_cost = float(m.group(2))
        latest_tokens = parse_shorthand_number(m.group(3))

    return total_cost, total_tokens, latest_cost, latest_tokens


def parse_memory_status(text: str):
    result = {}
    current = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith('Memory Search (') and line.endswith(')'):
            current = line[len('Memory Search ('):-1].strip().lower()
            result.setdefault(current, {'embeddings_ready': 0, 'indexed_files': 0, 'indexed_total': 0, 'chunks': 0})
            continue
        if not current:
            continue
        if line.startswith('Embeddings:'):
            result[current]['embeddings_ready'] = 1 if 'ready' in line.lower() else 0
        elif line.startswith('Indexed:'):
            m = re.search(r'Indexed:\s+(\d+)/(\d+) files · (\d+) chunks', line)
            if m:
                result[current]['indexed_files'] = int(m.group(1))
                result[current]['indexed_total'] = int(m.group(2))
                result[current]['chunks'] = int(m.group(3))
    return result


def parse_systemd_active(text: str) -> int:
    return 1 if text.strip() == 'active' else 0


def parse_recent_gateway_alerts(text: str):
    lowered = text.lower()
    duplicate = 1 if 'eaddrinuse' in lowered or 'another gateway instance is already listening' in lowered else 0
    rate_limit = 1 if 'usage limit' in lowered or 'reason=rate_limit' in lowered else 0
    return duplicate, rate_limit


def parse_fallback_count_from_config():
    config_path = Path('/root/.openclaw/openclaw.json')
    try:
        data = json.loads(config_path.read_text())
        fallbacks = (((data.get('agents') or {}).get('defaults') or {}).get('model') or {}).get('fallbacks') or []
        if isinstance(fallbacks, list):
            return len(fallbacks)
    except Exception:
        pass
    return 0


def main():
    global EMITTED_META
    EMITTED_META = set()
    lines = []
    now = int(time.time())
    exporter_success = 1

    health_rc, health_out = run(['openclaw', 'gateway', 'health'])
    probe_rc, probe_out = run(['openclaw', 'gateway', 'probe'])
    tasks_rc, tasks_out = run(['openclaw', 'tasks', 'list'])
    usage_rc, usage_out = run(['openclaw', 'gateway', 'usage-cost'])
    status_rc, status_out = run(['openclaw', 'status', '--deep'])
    memory_rc, memory_out = run(['openclaw', 'memory', 'status', '--deep'])
    system_gateway_rc, system_gateway_out = run(['systemctl', 'is-active', 'openclaw-gateway.service'])
    user_gateway_rc, user_gateway_out = run_shell('systemctl --user is-active openclaw-gateway.service 2>/dev/null || true')
    gateway_journal_rc, gateway_journal_out = run_shell("journalctl -u openclaw-gateway.service --since '-10 min' --no-pager 2>/dev/null | tail -n 400")

    health_ok, telegram_ok = parse_gateway_health(health_out)
    probe_ok, admin_capable = parse_gateway_probe(probe_out)
    tasks_total = parse_tasks(tasks_out)
    sessions_active, agents_count = parse_status(status_out)
    total_cost, total_tokens, latest_cost, latest_tokens = parse_usage(usage_out)
    fallback_count = parse_fallback_count_from_config()
    memory_by_agent = parse_memory_status(memory_out)
    system_gateway_active = parse_systemd_active(system_gateway_out)
    user_gateway_active = parse_systemd_active(user_gateway_out)
    duplicate_gateway_recent, gateway_rate_limit_recent = parse_recent_gateway_alerts(gateway_journal_out)

    lines += metric_lines('openclaw_gateway_health_ok', bool_metric(health_ok), '1 if openclaw gateway health reports OK')
    lines += metric_lines('openclaw_gateway_telegram_ok', bool_metric(telegram_ok), '1 if gateway health reports Telegram ok')
    lines += metric_lines('openclaw_gateway_probe_ok', bool_metric(probe_ok), '1 if openclaw gateway probe reports reachable/ok')
    lines += metric_lines('openclaw_gateway_capability_admin', bool_metric(admin_capable), '1 if gateway probe reports admin-capable')
    lines += metric_lines('openclaw_tasks_total', tasks_total, 'Current number of background tasks reported by openclaw tasks list')
    lines += metric_lines('openclaw_sessions_active', sessions_active, 'Approximate active session count parsed from openclaw status --deep')
    lines += metric_lines('openclaw_agents_count', agents_count, 'Approximate agent count parsed from openclaw status --deep')
    lines += metric_lines('openclaw_usage_cost_usd_30d', total_cost, '30-day OpenClaw usage cost in USD')
    lines += metric_lines('openclaw_usage_tokens_30d', int(total_tokens), '30-day OpenClaw token usage count')
    lines += metric_lines('openclaw_usage_cost_usd_latest_day', latest_cost, 'Latest daily OpenClaw usage cost in USD')
    lines += metric_lines('openclaw_usage_tokens_latest_day', int(latest_tokens), 'Latest daily OpenClaw token usage count')
    lines += metric_lines('openclaw_usage_command_available', bool_metric(usage_rc != 127), '1 if openclaw gateway usage-cost command exists')
    lines += metric_lines('openclaw_tasks_command_available', bool_metric(tasks_rc != 127), '1 if openclaw tasks list command exists')
    lines += metric_lines('openclaw_status_command_available', bool_metric(status_rc != 127), '1 if openclaw status --deep command exists')
    lines += metric_lines('openclaw_memory_status_command_available', bool_metric(memory_rc != 127), '1 if openclaw memory status --deep command exists')
    lines += metric_lines('openclaw_fallback_models_configured', fallback_count, 'Configured fallback model count from openclaw config')
    lines += metric_lines('openclaw_gateway_system_service_active', system_gateway_active, '1 if systemd system openclaw-gateway.service is active')
    lines += metric_lines('openclaw_gateway_user_service_active', user_gateway_active, '1 if systemd user openclaw-gateway.service is active')
    lines += metric_lines('openclaw_gateway_duplicate_supervisor_recent', duplicate_gateway_recent, '1 if gateway journal shows duplicate supervisor or EADDRINUSE in the last 10 minutes')
    lines += metric_lines('openclaw_gateway_rate_limit_recent', gateway_rate_limit_recent, '1 if gateway journal shows recent upstream rate limit errors in the last 10 minutes')

    for agent_name, parsed in sorted(memory_by_agent.items()):
        lines += metric_lines('openclaw_memory_embeddings_ready', parsed.get('embeddings_ready', 0), '1 if OpenClaw memory embeddings are ready for the agent', labels={'agent': agent_name})
        lines += metric_lines('openclaw_memory_indexed_files', parsed.get('indexed_files', 0), 'Indexed memory files reported by openclaw memory status --deep', labels={'agent': agent_name})
        lines += metric_lines('openclaw_memory_indexed_chunks', parsed.get('chunks', 0), 'Indexed memory chunks reported by openclaw memory status --deep', labels={'agent': agent_name})

    command_rcs = {
        'gateway_health': health_rc,
        'gateway_probe': probe_rc,
        'tasks_list': tasks_rc,
        'usage_cost': usage_rc,
        'status_deep': status_rc,
        'memory_status_deep': memory_rc,
        'systemctl_gateway_system': system_gateway_rc,
        'gateway_journal_recent': gateway_journal_rc,
    }
    lines.append('# HELP openclaw_command_last_rc Last return code for read-only OpenClaw exporter command')
    lines.append('# TYPE openclaw_command_last_rc gauge')
    for label, rc in command_rcs.items():
        lines.append(f'openclaw_command_last_rc{{command="{label}"}} {rc}')
        if rc not in (0, 127):
            exporter_success = 0

    if health_rc == 127 or probe_rc == 127:
        exporter_success = 0

    lines += metric_lines('openclaw_exporter_last_success_unixtime', now if exporter_success else 0, 'Unix timestamp of last successful exporter run')
    lines += metric_lines('openclaw_exporter_success', exporter_success, '1 if exporter command set completed without critical failures')

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', delete=False, dir=str(OUT.parent), prefix='.openclaw.', suffix='.prom') as tmp:
        tmp.write('\n'.join(lines) + '\n')
        tmp_path = tmp.name
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, OUT)
    os.chmod(OUT, 0o644)


if __name__ == '__main__':
    main()
