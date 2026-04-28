# OpenClaw AI Office v2

AI-powered research system for startup ideation, market analysis, competitive intelligence, CV matching, and educational opportunities.

## What You Get

- **17 research agents** (cron + isolated sessions + state)
- **126+ skills** (all with evals)
- **Web search** (SearXNG)
- **Excel/Google Sheets** for financial models
- **HTML reports** with evidence-based citations
- **Telegram notifications** with all artifacts
- **MinIO S3** for artifact sharing
- **Dashboard** on port 3456
- **Vector database** for semantic search and cross-domain knowledge

---

## Prerequisites

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | macOS 14+ or Ubuntu 22.04+ | macOS 15 / Ubuntu 24.04 |
| RAM | 8 GB | 16 GB |
| CPU | 4 cores | Apple Silicon M1+ / 8 cores |
| Disk | 50 GB SSD | 100 GB SSD |
| Docker | ✅ Required | ✅ |
| Python | 3.10+ | 3.12 |

---

## Quick Start (macOS)

```bash
# 1. Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install dependencies
brew install git curl python@3.12 docker docker-compose node

# 3. Clone this repo
git clone https://github.com/sidnevart/chappi-ai-office-v2.git

# 4. Start Docker Desktop (launch from Applications)
open /Applications/Docker.app

# 5. Run everything
cd chappi-ai-office-v2
bash install.sh  # One-click setup
```

---

## Quick Start (Ubuntu/Linux)

```bash
# 1. Install dependencies
sudo apt update && sudo apt install -y git curl python3 python3-pip python3-venv docker.io docker-compose nginx

# 2. Clone repo
git clone https://github.com/sidnevart/chappi-ai-office-v2.git

# 3. Run everything
cd chappi-ai-office-v2
bash install.sh
```

---

## Manual Setup (12 Steps)

### Step 1: Install OpenClaw

```bash
# macOS
brew tap openclaw/tap
brew install openclaw

# Ubuntu
git clone https://github.com/openclaw-ai/openclaw.git /opt/openclaw-stack
cd /opt/openclaw-stack && make install

# Enable Docker
sudo systemctl enable docker  # Linux only
sudo usermod -aG docker $USER  # Linux only
```

### Step 2: Setup Telegram Bot

1. Open @BotFather in Telegram
2. Send `/newbot`
3. Name: "Chappi AI Office"
4. Username: `chappi_ai_office_bot`
5. Get **BOT_TOKEN** (e.g., `7600176913:AAEbL8lDDB_1vSIm3bni2WB2jlSzusMwLxc`)
6. Create channel, add bot as admin
7. Get **CHAT_ID** (e.g., `-1003891142888`)

```bash
# Add to ~/.bashrc or ~/.zshrc:
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
export TELEGRAM_CHAT_ID="YOUR_CHAT_ID"
```

### Step 3: Setup Model (Ollama)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# macOS alternative:
brew install ollama

# Pull model
ollama pull kimi-k2.6:cloud

# Verify
ollama run kimi-k2.6:cloud "Hello"
```

### Step 4: Setup MinIO S3

```bash
# Docker (works on both macOS and Linux)
docker run -d \
  --name minio \
  -p 9000:9000 -p 9001:9001 \
  -v /mnt/minio:/data \
  -e MINIO_ROOT_USER=minio \
  -e MINIO_ROOT_PASSWORD=minio123 \
  minio/minio server /data --console-address :9001

# Create bucket
docker exec minio mc mb local/ai-office
docker exec minio mc policy set public local/ai-office
```

### Step 5: Setup Web Search (SearXNG)

```bash
# Docker
docker run -d \
  --name searxng \
  -p 8080:8080 \
  searxng/searxng

# Test
curl "http://localhost:8080/search?q=test"
```

### Step 6: Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install openpyxl reportlab boto3 python-telegram-bot sentence-transformers
```

### Step 7: Configure OpenClaw

```bash
# Create config
mkdir -p ~/.openclaw
cat > ~/.openclaw/config.yaml << 'EOF'
model: ollama/kimi-k2.6:cloud
gateway:
  port: 18789
  host: 0.0.0.0
memory:
  enabled: true
  path: ~/.openclaw/memory
EOF
```

### Step 8: Setup Cron Jobs

```bash
mkdir -p ~/.openclaw/cron
cat > ~/.openclaw/cron/jobs.json << 'EOF'
{
  "version": 1,
  "jobs": [
    {
      "name": "trend_monitor",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "0 6 * * *", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "trend-monitor"}
    },
    {
      "name": "business_deal_flow_tracker",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "30 6 * * *", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "deal-flow-tracker"}
    },
    {
      "name": "job_scout",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "30 8 * * *", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "job-scout"}
    },
    {
      "name": "weekly_matcher",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "0 9 * * 1", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "weekly-matcher"}
    },
    {
      "name": "idea_generator",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "30 10 * * 1", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "idea-generator"}
    },
    {
      "name": "company_analyst",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "0 11 * * 1", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "company-analyst-agent"}
    }
  ]
}
EOF
```

### Step 9: Copy Skills

```bash
cp -r skills/* /opt/openclaw-stack/workspace/skills/
```

### Step 10: Initialize Vector Database

```bash
mkdir -p /mnt/files/research-state/db
cat > /mnt/files/research-state/db/state.json << 'EOF'
{"version": "1.0", "entities": {}}
EOF
cat > /mnt/files/research-state/db/knowledge.json << 'EOF'
{"version": "1.0", "facts": {}, "relationships": {}}
EOF
cat > /mnt/files/research-state/db/feedback.json << 'EOF'
{"version": "1.0", "feedback": [], "preferences": {}}
EOF
```

### Step 11: Start Dashboard

```bash
cd /opt/openclaw-stack/workspace
node office/dashboard-server.js &
```

### Step 12: Verify Everything

```bash
# Check services
curl http://localhost:9000          # MinIO
curl http://localhost:8080          # SearXNG
curl http://localhost:18789/health  # OpenClaw
curl http://localhost:3456          # Dashboard

# Check Telegram
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe"

# Check model
ollama run kimi-k2.6:cloud "test"
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        OPENCLAW CORE                            │
│                    (Agent: main, telegram)                      │
├─────────────────────────────────────────────────────────────────┤
│  17 Cron Jobs                                                   │
│  ├── Daily 06:00-08:30 (trends, deals, edu, jobs)             │
│  └── Weekly Mon 09:00-11:00 (matcher, ideas, analysis)        │
├─────────────────────────────────────────────────────────────────┤
│  126 Skills (with evals)                                        │
│  ├── Research: trend-monitor, deal-flow-tracker               │
│  ├── Analysis: company-deep-dive, competitive-analysis          │
│  ├── Generation: idea-generator, pitch-builder                 │
│  ├── Finance: financial-modeling (Excel)                       │
│  ├── Scouts: job-scout, edu-*-scout                          │
│  └── Infrastructure: retry-handler, quality-gate            │
├─────────────────────────────────────────────────────────────────┤
│  Shared Systems                                                 │
│  ├── Vector DB (SQLite + embeddings)                           │
│  ├── State Persistence (JSON with TTL)                         │
│  ├── Knowledge Base (cross-agent facts)                        │
│  └── Feedback Loop (👍/👎 → preferences)                      │
├─────────────────────────────────────────────────────────────────┤
│  Outputs                                                        │
│  ├── HTML Reports → S3 → Telegram                            │
│  ├── Excel Models → S3 → Telegram                            │
│  ├── Pitches → S3 → Telegram                                  │
│  └── Dashboard: http://localhost:3456                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Cron Schedule (Moscow Time)

| Time | Job | Skill |
|------|-----|-------|
| 06:00 | Trend Monitor | `trend-monitor` |
| 06:30 | Deal Flow | `deal-flow-tracker` |
| 07:00 | Competition Scout | `edu-competition-scout` |
| 07:30 | Grant Scout | `edu-grant-scout` |
| 08:00 | Bootcamp Scout | `edu-bootcamp-scout` |
| 08:30 | Job Scout | `job-scout` |
| 09:00 | Weekly Matcher | `weekly-matcher` |
| 09:30 | Opportunity Matcher | `edu-opportunity-matcher` |
| 10:00 | Job Matcher | `job-matcher` |
| 10:30 | Idea Generator | `idea-generator` |
| 11:00 | Company Analyst | `company-analyst-agent` |

---

## API Keys & Secrets

| Service | Variable | Where to Get |
|---------|----------|--------------|
| Telegram Bot | `TELEGRAM_BOT_TOKEN` | @BotFather |
| Telegram Chat | `TELEGRAM_CHAT_ID` | Channel settings |
| MinIO | `MINIO_ROOT_PASSWORD` | Self-hosted |

---

## Ports

| Port | Service |
|------|---------|
| 18789 | OpenClaw Gateway |
| 3456 | Dashboard |
| 9000 | MinIO API |
| 9001 | MinIO Console |
| 8080 | SearXNG |
| 11434 | Ollama |

---

## Models

| Model | Usage | Install |
|-------|-------|---------|
| kimi-k2.6:cloud | Primary | `ollama pull` |
| all-MiniLM-L6-v2 | Embeddings | `pip install sentence-transformers` |

---

## Troubleshooting

### Model not responding
```bash
ollama ps              # Check running models
ollama pull kimi-k2.6:cloud  # Reinstall
```

### MinIO not accessible
```bash
docker logs minio
docker restart minio
```

### Telegram not sending
```bash
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe"
```

### Skills not found
```bash
ls /opt/openclaw-stack/workspace/skills/ | wc -l
# Should be 100+
```

---

## Stats

- **Skills:** 126
- **With evals:** 127
- **Agents:** 17 (12 cron + 5 on-demand)
- **Reports generated:** 10+
- **Pipeline steps:** 9 (Company → Pitch)
- **CV profile:** Artem Sidnev (3y exp, T-Bank, Java/Kotlin/Go/Python)

---

## Links

- **GitHub:** https://github.com/sidnevart/chappi-ai-office-v2
- **Dashboard:** http://localhost:3456
- **S3:** http://localhost:9000 (minio/minio123)

---

*OpenClaw AI Office v2 | 126 skills | 17 agents | Evidence-based research*