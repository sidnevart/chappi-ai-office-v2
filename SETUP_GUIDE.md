# OpenClaw AI Office — Setup Guide

Полная инструкция по развёртыванию AI Office с системой исследований.

## 🚀 Быстрый старт

```bash
# 1. Клонировать репозиторий
git clone https://github.com/sidnevart/chappi-ai-office-v2.git
cd chappi-ai-office-v2

# 2. Установить OpenClaw
npm install -g openclaw

# 3. Инициализировать
openclaw init
openclaw config set gateway.port 18789

# 4. Запустить gateway
openclaw gateway start

# 5. Установить зависимости
pip install pdfplumber ollama

# 6. Настроить Google Drive
openclaw toolkit add googledrive
# Следовать инструкциям OAuth

# 7. Создать папку cur_cv в Google Drive
# Загрузить CV в формате PDF

# 8. Запустить dashboard
node office/dashboard-server.js
# Dashboard доступен на http://localhost:3456/
```

## 📁 Структура

```
workspace/
├── skills/                    # 55+ скиллов
│   ├── deep-research/
│   ├── job-scout/
│   ├── company-deep-dive/
│   ├── idea-generator/
│   └── ...
├── office/
│   ├── index.html            # Dashboard UI
│   └── dashboard-server.js   # Сервер
├── memory/
│   └── YYYY-MM-DD.md         # Daily logs
├── plans/
│   └── research-system-plan.md
└── REPORTS/                  # Генерированные отчёты
```

## 🤖 Агенты (17 штук)

### Ежедневно (с 6:00 UTC+3)
| Время | Агент | Описание |
|-------|-------|----------|
| 06:00 | TrendMonitor | Тренды AI |
| 06:30 | DealFlow | Инвестиции |
| 07:00 | EduCompetition | Соревнования |
| 07:30 | EduGrant | Гранты |
| 08:00 | EduBootcamp | Буткемпы |
| 08:30 | JobScout | Вакансии |

### Еженедельно (Понедельник)
| Время | Агент | Описание |
|-------|-------|----------|
| 09:00 | WeeklyMatcher | Сопоставление |
| 09:30 | EduMatcher | Образование |
| 10:00 | JobMatcher | Работа |
| 10:30 | IdeaGenerator | Идеи |
| 11:00 | CompanyAnalyst | Анализ компаний |

## 🔄 Полный пайплайн

```bash
# Запустить весь пайплайн для идеи
openclaw agent run CompanyAnalyst --company="OpenAI"
openclaw agent run CompetitiveStrategist
openclaw agent run IdeaGenerator
openclaw agent run RussianMarketAnalyst
openclaw agent run FundingScout
openclaw agent run FinancialModeler
openclaw agent run PitchBuilder
openclaw agent run TechSpecWriter
```

## 📊 Dashboard

Dashboard запущен на порту 3456:
- **URL:** http://YOUR_IP:3456/
- **API:** http://YOUR_IP:3456/api/agents
- **Schedule:** http://YOUR_IP:3456/api/schedule

## 📝 Состояние системы

Все данные хранятся в `/mnt/files/research-state/`:
- `edu/` — образование
- `career/` — карьера
- `business/` — бизнес
- `logs/` — логи агентов

## 🔧 Настройка cron

```bash
# Редактировать cron jobs
openclaw cron edit

# Или напрямую
nano ~/.openclaw/cron/jobs.json
```

## 🌐 Доступ извне

```bash
# Открыть порт 3456
sudo ufw allow 3456/tcp

# Или через nginx
sudo cp nginx/ai-office.conf /etc/nginx/conf.d/
sudo nginx -t && sudo systemctl reload nginx
```

## 📦 Docker (опционально)

```bash
# Собрать образ
docker build -t chappi-ai-office .

# Запустить
docker run -d -p 3456:3456 -v $(pwd):/workspace chappi-ai-office
```

## 🔑 SSH ключ для GitHub

```bash
# Добавить публичный ключ в GitHub
# Settings -> SSH and GPG keys -> New SSH key
cat ~/.ssh/id_ed25519_github.pub
```

## 📞 Поддержка

- **OpenClaw docs:** https://openclaw.dev
- **Issues:** https://github.com/sidnevart/chappi-ai-office-v2/issues
- **Telegram:** @sidnevart_space_bot

---

*AI Office Research System | 17 агентов | OpenClaw v2.0*
