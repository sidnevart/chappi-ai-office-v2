# Chappi AI Office v2 — Полная инструкция по настройке

## Что это

AI Office — система исследований на базе OpenClaw с 17 агентами для анализа рынков, генерации идей, поиска инвестиций и создания pitch decks. Агенты работают автоматически по расписанию и отправляют результаты в Telegram.

---

## Системные требования

| Компонент | Минимум | Рекомендуемо |
|-----------|---------|--------------|
| CPU | 2 ядра | 4+ ядра |
| RAM | 4 GB | 8+ GB |
| Диск | 20 GB | 50+ GB SSD |
| OS | Ubuntu 22.04 | Ubuntu 24.04 LTS |
| Сеть | Публичный IP | Статический IP |

---

## Быстрый старт

```bash
# 1. Клонировать репозиторий
git clone https://github.com/sidnevart/chappi-ai-office-v2.git
cd chappi-ai-office-v2

# 2. Установить Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 3. Установить Python зависимости
pip install pdfplumber boto3 reportlab openpyxl pyyaml --break-system-packages

# 4. Установить OpenClaw
npm install -g openclaw

# 5. Инициализировать
openclaw init
openclaw config set gateway.port 18789
```

---

## Пошаговая настройка

### Шаг 1: OpenClaw Gateway (ядро системы)

```bash
# Проверить статус
openclaw gateway status

# Запустить если не запущен
openclaw gateway start

# Проверить порты (должен быть на 18789)
ss -tlnp | grep 18789

# Проверить конфиг
cat ~/.openclaw/openclaw.json | grep -A2 gateway
```

**Важно:** Gateway должен быть запущен 24/7. Рекомендуется systemd сервис:

```bash
# Создать systemd сервис
sudo tee /etc/systemd/system/openclaw-gateway.service << 'EOF'
[Unit]
Description=OpenClaw Gateway
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/openclaw gateway start
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable openclaw-gateway
sudo systemctl start openclaw-gateway
```

### Шаг 2: Cron Jobs (17 агентов)

```bash
# Проверить текущие задачи
openclaw cron list

# Редактировать
openclaw cron edit
```

**Расписание (UTC+3, Москва):**

| Время | Агент | Что делает |
|-------|-------|------------|
| 06:00 | TrendMonitor | Ищет тренды в AI |
| 06:30 | DealFlow | Отслеживает инвестиции |
| 07:00 | EduCompetition | Ищет хакатоны |
| 07:30 | EduGrant | Ищет гранты |
| 08:00 | EduBootcamp | Ищет буткемпы |
| 08:30 | JobScout | Ищет вакансии |
| 09:00 | WeeklyMatcher | Сопоставляет CV (Пн) |
| 09:30 | EduMatcher | Образовательные матчи (Пн) |
| 10:00 | JobMatcher | Рабочие матчи (Пн) |
| 10:30 | IdeaGenerator | Генерирует идеи (Пн) |
| 11:00 | CompanyAnalyst | Анализирует компании (Пн) |

**Важно:** Каждый агент запускается в изолированной сессии (`sessionTarget: "isolated"`). Это значит, что каждый агент получает чистое состояние.

### Шаг 3: Google Drive (для CV)

```bash
# Подключить Google Drive
openclaw toolkit add googledrive
```

**Что произойдёт:**
1. Откроется ссылка для OAuth авторизации
2. Нужно авторизоваться в Google
3. Разрешить доступ к Google Drive
4. Получить token и вставить в консоль

**После подключения:**
```bash
# Создать папку cur_cv в Google Drive
# Загрузить туда CV в формате PDF
```

**Проверка:**
```bash
# Скачать CV
openclaw agent run CVParser
# Должны появиться файлы в /mnt/files/research-state/
```

### Шаг 4: Composio (альтернатива Google Drive)

```bash
# Установить Composio
npm install -g composio

# Добавить toolkit
openclaw toolkit add composio

# Настроить Google Drive через Composio
composio add googledrive
```

**Почему Composio:**
- Проще авторизация
- Больше интеграций
- Лучше для автоматизации

### Шаг 5: MinIO (S3 хранилище)

```bash
# Установить Docker
curl -fsSL https://get.docker.com | sh

# Запустить MinIO
docker run -d --name minio-ai-office \
  -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minio \
  -e MINIO_ROOT_PASSWORD=minio123 \
  -v /mnt/data/minio:/data \
  minio/minio server /data --console-address ":9001"

# Создать bucket
pip install boto3 --break-system-packages
python3 << 'PYEOF'
import boto3
from botocore.config import Config
s3 = boto3.client('s3',
    endpoint_url='http://127.0.0.1:9000',
    aws_access_key_id='minio',
    aws_secret_access_key='minio123',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)
s3.create_bucket(Bucket='ai-office')
print("✅ Bucket создан")
PYEOF

# Открыть порт в фаерволе
sudo ufw allow 9000/tcp
sudo ufw allow 9001/tcp
```

**Проверка:** http://80.74.25.43:9000/ai-office/

### Шаг 6: Dashboard (веб-интерфейс)

```bash
# Dashboard запущен на порту 3456
# Проверить
ss -tlnp | grep 3456

# Если не запущен:
nohup node /tmp/ai-office-dashboard.js > /tmp/ai-office.log 2>&1 &
echo $! > /tmp/ai-office.pid

# Открыть порт
sudo ufw allow 3456/tcp
```

**URL:** http://80.74.25.43:3456/

**Что показывает:**
- Список всех 17 агентов
- Статус каждого (active/running/pending)
- Расписание запусков
- Метрики (найдено трендов, сделок, вакансий)
- Логи коммуникаций между агентами

### Шаг 7: Telegram (уведомления)

```bash
# Проверить конфиг
cat ~/.openclaw/openclaw.json | python3 -m json.tool | grep -A10 telegram
```

**Настройка:**
1. Написать @BotFather
2. Создать нового бота
3. Получить token
4. Добавить бота в канал
5. Получить chat_id

**Конфигурация в openclaw.json:**
```json
{
  "channels": {
    "telegram": {
      "accounts": {
        "telegram-main": {
          "name": "Telegram",
          "enabled": true,
          "tokenFile": "/opt/openclaw-stack/secrets/telegram-bot-token"
        }
      },
      "enabled": true
    }
  }
}
```

**Проверка:**
```bash
# Отправить тестовое сообщение
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage" \
  -d "chat_id=YOUR_CHAT_ID" \
  -d "text=Test message"
```

---

## Структура системы

```
/opt/openclaw-stack/workspace/
├── skills/                    # 55+ скиллов
│   ├── trend-monitor/
│   │   ├── SKILL.md           # Инструкция для агента
│   │   └── evals/
│   │       └── basic.yaml     # Тесты
│   ├── deal-flow-tracker/
│   ├── company-deep-dive/
│   └── ...
├── office/
│   ├── index.html             # Dashboard UI
│   └── dashboard-server.js    # Сервер
├── memory/
│   └── 2026-04-28.md          # Логи
├── plans/
│   └── research-system-plan.md
└── README.md
```

---

## Форматы данных

### JSON (для агентов)
- Машинная обработка
- Фиксированная структура
- Pipeline между агентами

### HTML (для людей)
- Красивые таблицы
- Метрики и графики
- Публичные URL через S3

### Excel (для финансов)
- Финансовые модели
- Таблицы с формулами
- Графики

### PDF (для печати)
- Конвертация HTML → PDF
- Через ReportLab
- С поддержкой кириллицы

### Markdown (для документации)
- Технические спецификации
- GitHub-friendly

---

## Pipeline агентов

```
TrendMonitor ──→ DealFlow ──→ CompanyAnalyst ──→ IdeaGenerator
     │                │                │                  │
     ▼                ▼                ▼                  ▼
  trends.json    deals.json      companies/*.json    ideas.json
     │                │                │                  │
     ▼                ▼                ▼                  ▼
  trends.html     deals.html     companies/*.html    ideas.html
     │                │                │                  │
     └────────────────┴────────────────┴──────────────────┘
                             │
                             ▼
                    S3 Upload (MinIO)
                             │
                             ▼
                    Telegram Notification
```

---

## Типичные проблемы и решения

### Проблема: Агенты не видны в OpenClaw Office

**Причина:** OpenClaw Office (https://80.74.25.43:8443/office/) показывает только сконфигурированных агентов (main, telegram). Наши агенты — это cron jobs.

**Решение:** Использовать отдельный dashboard на порту 3456: http://80.74.25.43:3456/

### Проблема: S3 файлы не доступны (NoSuchKey)

**Причина:** Файлы не загружены в MinIO.

**Решение:**
```bash
# Проверить MinIO
curl http://127.0.0.1:9000/ai-office/

# Перезагрузить файлы
python3 scripts/upload-all-to-s3.py
```

### Проблема: PDF с квадратами вместо текста

**Причина:** Нет шрифтов с кириллицей.

**Решение:**
```bash
# Установить шрифты
apt-get install -y fonts-dejavu

# Проверить
ls /usr/share/fonts/truetype/dejavu/

# Использовать ReportLab (не playwright)
```

### Проблема: Cron jobs не запускаются

**Причина:** Gateway не запущен или jobs disabled.

**Решение:**
```bash
# Проверить gateway
openclaw gateway status

# Проверить jobs
cat ~/.openclaw/cron/jobs.json | python3 -m json.tool | grep enabled

# Включить
cat ~/.openclaw/cron/jobs.json | python3 -c "
import json, sys
data = json.load(sys.stdin)
for j in data['jobs']:
    j['enabled'] = True
json.dump(data, sys.stdout, indent=2)
" > /tmp/jobs.json
cp /tmp/jobs.json ~/.openclaw/cron/jobs.json
```

### Проблема: Composio не подключается

**Причина:** Нет активного соединения.

**Решение:**
```bash
# Проверить статус
composio status

# Переподключить
composio add googledrive

# Проверить в openclaw
openclaw toolkit list
```

---

## Evals (тестирование скиллов)

### Структура

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

### Запуск

```bash
# Проверить все evals
python3 scripts/run-all-evals.py

# Или вручную для одного скилла
python3 skills/skill-evaluator/eval.py --skill=trend-monitor
```

### Типы проверок

| Check | Описание |
|-------|----------|
| `contains` | Содержит текст |
| `has_fields` | Есть поля JSON |
| `json_output` | Валидный JSON |
| `file_exists` | Файл создан |
| `score_range` | Значение в диапазоне |

---

## Команды управления

```bash
# Gateway
openclaw gateway start|stop|status|restart

# Cron
openclaw cron list
openclaw cron edit
openclaw cron enable|disable {job-name}

# Agents
openclaw agent list
openclaw agent run {name}

# Skills
openclaw skill list
openclaw skill reload

# Toolkit
openclaw toolkit list
openclaw toolkit add {name}
```

---

## Доступ к артефактам

| Тип | URL | Формат |
|-----|-----|--------|
| Dashboard | http://80.74.25.43:3456/ | HTML |
| MinIO S3 | http://80.74.25.43:9000/ai-office/ | Various |
| Gateway | https://80.74.25.43:8443/ | OpenClaw UI |

---

## Обновление системы

```bash
# Обновить код
cd /opt/openclaw-stack/workspace
git pull origin master

# Перезагрузить skills
openclaw skill reload

# Перезапустить gateway
openclaw gateway restart

# Проверить статус
openclaw gateway status
```

---

## Поддержка

- **GitHub:** https://github.com/sidnevart/chappi-ai-office-v2
- **Issues:** Создавать issue в GitHub
- **Dashboard:** http://80.74.25.43:3456/

---

*AI Office Research System | 17 агентов | OpenClaw v2.0*
