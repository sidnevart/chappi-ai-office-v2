# OpenClaw AI Office — Setup Guide

Полная инструкция по настройке OpenClaw с системой исследований (Research System).

---

## 1. Установка OpenClaw

### Требования
- Ubuntu 22.04+ / Debian 12+
- 4 CPU, 8GB RAM, 50GB SSD
- Docker + Docker Compose
- Node.js 22+

### Установка

```bash
# 1. Установить Node.js 22
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. Установить OpenClaw
npm install -g openclaw

# 3. Инициализировать
openclaw init
openclaw config set gateway.port 18789

# 4. Запустить gateway
openclaw gateway start
```

---

## 2. Настройка Research System

### 2.1 Склонировать репозиторий скиллов

```bash
# Создать workspace
cd /opt
sudo mkdir openclaw-stack
sudo chown $USER:$USER openclaw-stack
cd openclaw-stack

# Склонировать скиллы
git clone https://github.com/your-repo/openclaw-research-skills.git workspace/
```

### 2.2 Установить superpowers скиллы

```bash
cd /tmp
git clone --depth 1 https://github.com/obra/superpowers.git

# Копируем скиллы
cp -r superpowers/skills/test-driven-development /opt/openclaw-stack/workspace/skills/sp-tdd
cp -r superpowers/skills/systematic-debugging /opt/openclaw-stack/workspace/skills/sp-systematic-debugging
cp -r superpowers/skills/writing-skills /opt/openclaw-stack/workspace/skills/sp-writing-skills
# ... и остальные
```

### 2.3 Установить eval-инфраструктуру

```bash
mkdir -p /opt/openclaw-stack/workspace/skills/skill-evaluator/evals
# Скопировать eval.yaml из репозитория
```

---

## 3. Настройка агентов

### 3.1 Создать cron jobs

```bash
# Открыть cron editor
openclaw cron edit

# Добавить jobs (см. agents.yaml в репозитории)
# Все агенты разнесены по времени с интервалом 30 минут
```

### 3.2 Пример cron job

```json
{
  "name": "TrendMonitor",
  "enabled": true,
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Europe/Moscow"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Запусти агента TrendMonitor: загрузи skill trend-monitor-agent, выполни workflow.",
    "model": "ollama/kimi-k2.6:cloud",
    "timeoutSeconds": 300
  }
}
```

---

## 4. Настройка Google Drive

### 4.1 Подключить Google Drive

```bash
openclaw toolkit add googledrive
# Следовать инструкциям OAuth
```

### 4.2 Создать папку cur_cv

В Google Drive создать папку `cur_cv` и загрузить CV в формате PDF.

---

## 5. Настройка Telegram

### 5.1 Создать бота

1. Написать @BotFather
2. Создать нового бота
3. Получить token

### 5.2 Настроить OpenClaw

```bash
openclaw config set telegram.bot_token YOUR_TOKEN
openclaw config set telegram.chat_id YOUR_CHAT_ID
```

---

## 6. Структура директорий

```
/opt/openclaw-stack/workspace/
├── skills/                    # 55+ скиллов
│   ├── deep-research/
│   ├── job-scout/
│   ├── company-deep-dive/
│   ├── sp-tdd/               # superpowers
│   └── ...
├── office/
│   └── index.html            # Dashboard
├── memory/
│   └── YYYY-MM-DD.md         # Daily logs
├── plans/
│   └── research-system-plan.md
└── REPORTS/                  # Generated reports
```

---

## 7. Проверка работы

### 7.1 Запустить агента вручную

```bash
openclaw agent run TrendMonitor
```

### 7.2 Проверить state

```bash
ls -la /mnt/files/research-state/
cat /mnt/files/research-state/logs/agent-activity.json
```

### 7.3 Открыть dashboard

```
http://YOUR_IP:8081/office/
```

---

## 8. Полный пайплайн (пример)

```bash
# Запустить полный бизнес-анализ
openclaw agent run CompanyAnalyst --company="OpenAI"
openclaw agent run CompetitiveStrategist --input=business/companies/openai.json
openclaw agent run IdeaGenerator --trigger="OpenAI weakness"
openclaw agent run RussianMarketAnalyst --idea="vertical-ai"
openclaw agent run FundingScout --idea="vertical-ai"
openclaw agent run FinancialModeler --idea="vertical-ai"
openclaw agent run PitchBuilder --idea="vertical-ai"
openclaw agent run TechSpecWriter --idea="vertical-ai"
```

---

## 9. Техническая поддержка

- **OpenClaw docs:** https://openclaw.dev
- **Skills repo:** https://github.com/your-repo/openclaw-research-skills
- **Issues:** Создавать в GitHub issues

---

## 10. Обновление

```bash
cd /opt/openclaw-stack/workspace
git pull origin main
openclaw skills reload
openclaw gateway restart
```

---

*AI Office Research System | OpenClaw | 2026*
