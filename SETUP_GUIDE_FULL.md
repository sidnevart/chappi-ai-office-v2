# Chappi AI Office v2 — Полная инструкция по настройке

## Что это

AI Office — система исследований на базе OpenClaw с 17 агентами для анализа рынков, генерации идей, поиска инвестиций и создания pitch decks.

---

## Быстрый старт

```bash
# 1. Клонировать репозиторий
git clone https://github.com/sidnevart/chappi-ai-office-v2.git
cd chappi-ai-office-v2

# 2. Установить зависимости
npm install -g openclaw
pip install pdfplumber boto3 reportlab openpyxl --break-system-packages

# 3. Настроить OpenClaw
openclaw init
openclaw config set gateway.port 18789

# 4. Запустить gateway
openclaw gateway start
```

---

## Пошаговая настройка

### Шаг 1: OpenClaw Gateway

```bash
# Проверить статус
openclaw gateway status

# Запустить если не запущен
openclaw gateway start

# Проверить порты
ss -tlnp | grep openclaw
```

Должно быть: `127.0.0.1:18789` (gateway)

### Шаг 2: Cron Jobs (Агенты)

```bash
# Проверить cron jobs
openclaw cron list

# Редактировать
openclaw cron edit

# Или напрямую
nano ~/.openclaw/cron/jobs.json
```

**Важно:** Агенты запускаются через cron с `sessionTarget: "isolated"`. Это значит каждый агент запускается в изолированной сессии.

**Расписание (UTC+3):**
- 06:00 — TrendMonitor
- 06:30 — DealFlow
- 07:00 — EduCompetition
- 07:30 — EduGrant
- 08:00 — EduBootcamp
- 08:30 — JobScout
- 09:00 — WeeklyMatcher (Mon)
- 09:30 — EduMatcher (Mon)
- 10:00 — JobMatcher (Mon)
- 10:30 — IdeaGenerator (Mon)
- 11:00 — CompanyAnalyst (Mon)

### Шаг 3: Google Drive (CV)

```bash
# Подключить Google Drive
openclaw toolkit add googledrive
# Следовать инструкциям OAuth

# Создать папку cur_cv
# Загрузить CV в формате PDF
```

### Шаг 4: MinIO (S3)

```bash
# Запустить MinIO
docker run -d --name minio-ai-office \
  -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minio \
  -e MINIO_ROOT_PASSWORD=minio123 \
  -v /mnt/data/minio:/data \
  minio/minio server /data --console-address ":9001"

# Создать bucket
python3 -c "
import boto3
s3 = boto3.client('s3', endpoint_url='http://127.0.0.1:9000', aws_access_key_id='minio', aws_secret_access_key='minio123')
s3.create_bucket(Bucket='ai-office')
"
```

**Доступ:** http://80.74.25.43:9000/ai-office/

### Шаг 5: Composio (для CV parser)

```bash
# Composio уже настроен в системе
# Проверить подключение
ls ~/.openclaw/toolkits/ | grep google

# Должно быть: googledrive
```

### Шаг 6: Dashboard

```bash
# Dashboard запущен на порту 3456
# Проверить
ss -tlnp | grep 3456

# Если не запущен:
nohup node /tmp/ai-office-dashboard.js > /tmp/ai-office.log 2>&1 &
echo $! > /tmp/ai-office.pid
```

**URL:** http://80.74.25.43:3456/

### Шаг 7: Telegram

```bash
# Проверить конфиг
cat ~/.openclaw/openclaw.json | grep -A5 telegram

# Должно быть настроено:
# - tokenFile: /opt/openclaw-stack/secrets/telegram-bot-token
# - channel: -1003891142888
```

---

## Структура файлов

```
workspace/
├── skills/                    # 55+ скиллов
│   ├── trend-monitor/
│   │   ├── SKILL.md
│   │   └── evals/basic.yaml   # Тесты для скилла
│   ├── deal-flow-tracker/
│   ├── company-deep-dive/
│   └── ...
├── office/
│   ├── index.html             # Dashboard UI
│   └── dashboard-server.js    # Сервер (порт 3456)
├── REPORTS/                   # Генерированные отчёты
│   ├── team-memory-ai-report-v2.md
│   └── team-memory-ai-report.html
├── memory/                    # Daily logs
│   └── 2026-04-28.md
├── plans/                     # Research plans
├── state/                     # State files
└── README.md                  # Этот файл
```

---

## Форматы данных

### JSON → Читаемые форматы

Система использует JSON для машинной обработки, но генерирует:

| JSON источник | Читаемый формат | Где найти |
|---------------|----------------|-----------|
| `business/ideas/*.json` | Markdown отчёт | `REPORTS/*.md` |
| `business/financial_models/*.json` | Excel | `reports/excel/*.xlsx` |
| `business/pitches/*.html` | HTML pitch deck | `business/pitches/*.html` |
| `business/*.json` | PDF отчёт | `reports/pdf/*.pdf` |
| `tech-specs/*.md` | Markdown | `tech-specs/*.md` |

### Почему JSON?

- **Машинная обработка:** Агенты читают/пишут JSON программно
- **Структура:** Фиксированные поля, валидация
- **Пайплайн:** Один агент пишет JSON, другой читает
- **История:** Версионирование, diff

### Как читать

```bash
# JSON → pretty print
cat business/ideas/team-memory-ai.json | python3 -m json.tool

# JSON → CSV (для таблиц)
python3 -c "import json, csv; data=json.load(open('file.json')); ..."

# JSON → Excel
# Использовать openpyxl (скилл excel-builder)
```

---

## Тестирование скиллов (Evals)

### Структура eval

```yaml
# skills/trend-monitor/evals/basic.yaml
eval_id: trend-monitor-basic
skill: trend-monitor
cases:
  - id: detect-ai-trend
    input:
      query: "AI trends 2026"
    expected:
      - contains: "AI"
      - json_output: true
      - has_fields: ["trends", "scan_date"]
```

### Запуск evals

```bash
# Вручную (через Python)
python3 skills/skill-evaluator/eval.py --skill=trend-monitor

# Или через OpenClaw
openclaw skill eval trend-monitor
```

### Создание eval

1. Создать `skills/{skill}/evals/basic.yaml`
2. Определить input + expected checks
3. Запустить и проверить

### Типы проверок

| Check | Описание | Пример |
|-------|----------|--------|
| `contains` | Содержит текст | `contains: "AI"` |
| `has_fields` | Есть поля JSON | `has_fields: ["trend"]` |
| `json_output` | Валидный JSON | `json_output: true` |
| `file_exists` | Файл создан | `file_exists: "path"` |
| `score_range` | Значение в диапазоне | `score_range: [0, 10]` |

---

## Типичные проблемы

### Проблема: Агенты не видны в OpenClaw Office

**Причина:** OpenClaw Office показывает только сконфигурированных агентов (main, telegram). Наши агенты — это cron jobs.

**Решение:** Использовать отдельный dashboard на порту 3456.

### Проблема: S3 файлы не доступны

**Причина:** MinIO bucket не создан или файлы не загружены.

**Решение:**
```bash
# Проверить MinIO
curl http://127.0.0.1:9000/ai-office/

# Перезагрузить файлы
python3 scripts/upload-to-s3.py
```

### Проблема: PDF не генерируется

**Причина:** Нет шрифтов с кириллицей или playwright не установлен.

**Решение:**
```bash
# Установить шрифты
apt-get install fonts-dejavu

# Использовать ReportLab (без браузера)
pip install reportlab
```

### Проблема: Cron jobs не запускаются

**Причина:** Gateway не запущен или jobs не enabled.

**Решение:**
```bash
# Проверить
openclaw gateway status
openclaw cron list

# Включить
openclaw cron enable {job-name}
```

---

## Полный пайплайн (пример)

```bash
# 1. Запустить все агенты вручную
openclaw agent run TrendMonitor
openclaw agent run DealFlowTracker
openclaw agent run CompanyAnalyst --company="OpenAI"
openclaw agent run CompetitiveStrategist
openclaw agent run IdeaGenerator
openclaw agent run RussianMarketAnalyst
openclaw agent run FundingScout
openclaw agent run FinancialModeler
openclaw agent run PitchBuilder
openclaw agent run TechSpecWriter

# 2. Сгенерировать отчёты
openclaw skill html-to-pdf --input=pitches/team-memory-ai.html --output=reports/pdf/
openclaw skill excel-builder --input=financial_models/team-memory-ai.json --output=reports/excel/

# 3. Загрузить в S3
openclaw skill s3-uploader --files=reports/ --bucket=ai-office

# 4. Отправить в Telegram
openclaw skill telegram-reporter --report=team-memory-ai
```

---

## Доступ к артефактам

| Тип | URL | Локально |
|-----|-----|----------|
| Dashboard | http://80.74.25.43:3456/ | — |
| MinIO S3 | http://80.74.25.43:9000/ai-office/ | — |
| PDF отчёт | http://80.74.25.43:9000/ai-office/reports/*.pdf | `reports/pdf/` |
| Excel | http://80.74.25.43:9000/ai-office/reports/*.xlsx | `reports/excel/` |
| Pitch deck | http://80.74.25.43:9000/ai-office/pitches/*.html | `business/pitches/` |
| ТЗ | http://80.74.25.43:9000/ai-office/tech-specs/*.md | `tech-specs/` |

---

## Поддержка

- **GitHub:** https://github.com/sidnevart/chappi-ai-office-v2
- **Issues:** Создавать issue в GitHub
- **Dashboard:** http://80.74.25.43:3456/

---

*AI Office Research System | 17 agents | OpenClaw v2.0*
