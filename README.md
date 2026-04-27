# Chappi AI Office v2

AI-powered research system for startup ideation, market analysis, and competitive intelligence.

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/sidnevart/chappi-ai-office-v2.git
cd chappi-ai-office-v2

# Install dependencies
npm install -g openclaw
pip install pdfplumber playwright boto3
playwright install chromium

# Configure OpenClaw
openclaw init
openclaw config set gateway.port 18789

# Start services
openclaw gateway start
node office/dashboard-server.js  # Dashboard on port 3456

# Start MinIO (optional, for S3 uploads)
docker run -d -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minio \
  -e MINIO_ROOT_PASSWORD=minio123 \
  minio/minio server /data --console-address ":9001"
```

## 📊 Dashboard

Access the research dashboard at:
- **URL:** http://80.74.25.43:3456/
- **API:** http://80.74.25.43:3456/api/agents
- **Schedule:** http://80.74.25.43:3456/api/schedule

## 🤖 Agents (17 total)

### Daily (06:00 - 08:30 UTC+3)
| Time | Agent | Description |
|------|-------|-------------|
| 06:00 | TrendMonitor | AI trends, bioengineering |
| 06:30 | DealFlow | Startup funding tracking |
| 07:00 | EduCompetition | Competitions & hackathons |
| 07:30 | EduGrant | Grants & scholarships |
| 08:00 | EduBootcamp | Bootcamps & schools |
| 08:30 | JobScout | AI/Backend/DevOps jobs |

### Weekly (Monday, 09:00 - 11:00)
| Time | Agent | Description |
|------|-------|-------------|
| 09:00 | WeeklyMatcher | CV matching |
| 09:30 | EduMatcher | Education matching |
| 10:00 | JobMatcher | Job matching |
| 10:30 | IdeaGenerator | Business ideas |
| 11:00 | CompanyAnalyst | Company analysis |

## 🔄 Full Pipeline

```bash
# Run complete business analysis
openclaw agent run CompanyAnalyst --company="OpenAI"
openclaw agent run CompetitiveStrategist
openclaw agent run IdeaGenerator
openclaw agent run RussianMarketAnalyst
openclaw agent run FundingScout
openclaw agent run FinancialModeler
openclaw agent run PitchBuilder
openclaw agent run TechSpecWriter
```

## 📁 Structure

```
workspace/
├── skills/              # 55+ skills (rewritten with writing-skills standard)
├── office/              # Dashboard UI
├── REPORTS/             # Generated reports
├── memory/              # Daily logs
└── plans/               # Research plans
```

## 📝 Reports

| Report | File |
|--------|------|
| TeamMemory AI | [REPORTS/team-memory-ai-report-v2.md](REPORTS/team-memory-ai-report-v2.md) |
| Setup Guide | [SETUP_GUIDE.md](SETUP_GUIDE.md) |

## 🔧 Configuration

### S3 (MinIO)
```yaml
# ~/.openclaw/skills/s3-uploader/config.yaml
s3:
  endpoint: "http://localhost:9000"
  bucket: "ai-office"
  access_key: "minio"
  secret_key: "minio123"
```

### Cron Schedule
```bash
openclaw cron edit
# Or edit directly:
# ~/.openclaw/cron/jobs.json
```

## 🧪 Testing Skills

```bash
# Run skill evals
openclaw skill eval trend-monitor
openclaw skill eval deal-flow-tracker
```

## 📞 Support

- **Issues:** https://github.com/sidnevart/chappi-ai-office-v2/issues
- **Dashboard:** http://80.74.25.43:3456/

---

*AI Office Research System | 17 agents | OpenClaw v2.0*
