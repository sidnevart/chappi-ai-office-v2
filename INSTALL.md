# OpenClaw AI Office — Полная инструкция по установке

## Что получится

Автономная система исследований (AI Office) с:
- **17 агентами** (cron + скиллы + state)
- **126 скиллами** (все с evals)
- **Веб-поиском** (SearXNG)
- **Excel/Google Sheets** для финмоделей
- **HTML-отчётами** с evidence
- **Telegram-уведомлениями**
- **MinIO S3** для артефактов
- **Dashboard** на порту 3456

---

## Требования

| Компонент | Минимум | Рекомендуемо |
|-----------|---------|--------------|
| OS | Ubuntu 22.04+ | Ubuntu 24.04 |
| RAM | 8 GB | 16 GB |
| CPU | 4 cores | 8 cores |
| Disk | 50 GB SSD | 100 GB SSD |
| Docker | ✅ Required | ✅ |
| Python | 3.10+ | 3.12 |

---

## Шаг 1: Установка OpenClaw

```bash
# 1. Установка зависимостей
sudo apt update
sudo apt install -y git curl python3 python3-pip python3-venv docker.io docker-compose nginx

# 2. Клонирование OpenClaw
git clone https://github.com/openclaw-ai/openclaw.git /opt/openclaw-stack

# 3. Установка
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Перелогиниться для применения группы Docker

# 4. Запуск
cd /opt/openclaw-stack
make install  # или следовать README.md
```

---

## Шаг 2: Настройка GitHub

```bash
# 1. Создать репозиторий на GitHub (e.g., chappi-ai-office)
# 2. Клонировать
git clone https://github.com/YOUR_USERNAME/chappi-ai-office.git /opt/openclaw-stack/workspace

# 3. Или синхронизировать существующий
# (скопировать все файлы из текущего workspace)
cp -r /opt/openclaw-stack/workspace/* /opt/openclaw-stack/workspace/
```

---

## Шаг 3: Настройка MinIO S3

```bash
# 1. Запуск MinIO (Docker)
docker run -d \
  --name minio \
  -p 9000:9000 \
  -p 9001:9001 \
  -v /mnt/minio:/data \
  -e MINIO_ROOT_USER=minio \
  -e MINIO_ROOT_PASSWORD=minio123 \
  minio/minio server /data --console-address :9001

# 2. Создание bucket
docker exec minio mc alias set local http://localhost:9000 minio minio123
docker exec minio mc mb local/ai-office

# 3. Публичная политика
docker exec minio mc policy set public local/ai-office
```

---

## Шаг 4: Настройка Telegram

### 4.1 Создание бота
1. Откройте @BotFather в Telegram
2. Отправьте `/newbot`
3. Введите имя (e.g., "Chappi AI Office")
4. Введите username (e.g., "chappi_ai_office_bot")
5. Получите **BOT_TOKEN** (например: `7600176913:AAEbL8lDDB_1vSIm3bni2WB2jlSzusMwLxc`)

### 4.2 Создание канала
1. Создайте канал в Telegram (e.g., "@chappi_ai_office_digest")
2. Добавьте бота администратором
3. Получите **CHAT_ID** (e.g., `-1003891142888`)

### 4.3 Настройка
```bash
# Добавьте в ~/.bashrc или ~/.zshrc:
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
export TELEGRAM_CHAT_ID="YOUR_CHAT_ID"

# Или в secrets:
echo "TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN" > /opt/openclaw-stack/.env
echo "TELEGRAM_CHAT_ID=YOUR_CHAT_ID" >> /opt/openclaw-stack/.env
```

---

## Шаг 5: Настройка модели

### 5.1 Локальная модель (Ollama)

```bash
# Установка Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Запуск
systemctl enable ollama
systemctl start ollama

# Скачивание модели
ollama pull kimi-k2.6:cloud

# Проверка
ollama run kimi-k2.6:cloud "Hello"
```

### 5.2 Или API модель (OpenAI, Anthropic)

```bash
# Добавьте API ключи
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Или в ~/.openclaw/config.yaml:
# model: openai/gpt-4o
# api_key: ${OPENAI_API_KEY}
```

---

## Шаг 6: Настройка веб-поиска (SearXNG)

```bash
# Установка SearXNG
docker run -d \
  --name searxng \
  -p 8080:8080 \
  -v /mnt/searxng:/etc/searxng \
  searxng/searxng

# Проверка
curl "http://localhost:8080/search?q=test"

# В скиллах используется как:
# web_search(query="...")
```

---

## Шаг 7: Установка Python зависимостей

```bash
# Создание venv
python3 -m venv /opt/openclaw-stack/venv
source /opt/openclaw-stack/venv/bin/activate

# Установка зависимостей
pip install openpyxl reportlab boto3 python-telegram-bot sentence-transformers

# Для векторной БД
pip install faiss-cpu  # или faiss-gpu для GPU
```

---

## Шаг 8: Синхронизация скиллов

```bash
# Клонирование скиллов
git clone https://github.com/sidnevart/chappi-ai-office-v2.git /tmp/ai-office-skills

# Копирование скиллов
mkdir -p /opt/openclaw-stack/workspace/skills
cp -r /tmp/ai-office-skills/skills/* /opt/openclaw-stack/workspace/skills/

# Проверка
ls /opt/openclaw-stack/workspace/skills/ | wc -l
# Должно быть ~120+ скиллов
```

---

## Шаг 9: Настройка Cron Jobs

```bash
# OpenClaw автоматически загружает cron из файла
# Но нужно убедиться, что путь правильный

# Создать/отредактировать:
mkdir -p ~/.openclaw/cron
cat > ~/.openclaw/cron/jobs.json << 'EOF'
{
  "version": 1,
  "jobs": [
    {
      "name": "trend_monitor",
      "description": "AI trend monitoring",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "0 6 * * *", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "trend-monitor"}
    },
    {
      "name": "business_deal_flow_tracker",
      "description": "Track VC deals",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "30 6 * * *", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "deal-flow-tracker"}
    },
    {
      "name": "idea_generator",
      "description": "Generate startup ideas",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "30 10 * * 1", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "idea-generator"}
    },
    {
      "name": "company_analyst",
      "description": "Full pipeline analysis",
      "enabled": true,
      "schedule": {"kind": "cron", "expr": "0 11 * * 1", "tz": "Europe/Moscow"},
      "sessionTarget": "isolated",
      "payload": {"skill": "company-analyst-agent"}
    }
  ]
}
EOF

# Перезапуск OpenClaw для применения
sudo systemctl restart openclaw-gateway
```

---

## Шаг 10: Запуск Dashboard

```bash
# Dashboard уже настроен в /opt/openclaw-stack/workspace/office/index.html
# Или запустить Node.js сервер:

cd /opt/openclaw-stack/workspace
cat > dashboard.js << 'EOF'
const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  fs.readFile('office/index.html', (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Not found');
    } else {
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(data);
    }
  });
});

server.listen(3456, '0.0.0.0', () => {
  console.log('Dashboard: http://0.0.0.0:3456');
});
EOF

node dashboard.js &
```

---

## Шаг 11: Проверка

```bash
# 1. OpenClaw работает
curl http://localhost:8080/health  # или порт OpenClaw

# 2. Модель отвечает
ollama run kimi-k2.6:cloud "test"

# 3. S3 доступен
curl http://localhost:9000

# 4. Telegram бот работает
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe"

# 5. Скиллы загружены
ls /opt/openclaw-stack/workspace/skills/ | head -10

# 6. Cron jobs активны
cat ~/.openclaw/cron/jobs.json | python3 -m json.tool
```

---

## Шаг 12: Первый запуск

```bash
# Запустить pipeline вручную для проверки
cd /opt/openclaw-stack/workspace
python3 -m openclaw run-skill trend-monitor

# Проверить результаты
ls /mnt/files/research-state/business/trends.json
ls /mnt/files/research-state/reports/html/

# Проверить Telegram
# Должно прийти сообщение с отчётом
```

---

## API Ключи и Секреты

| Сервис | Переменная | Где получить |
|--------|-----------|--------------|
| Telegram | `TELEGRAM_BOT_TOKEN` | @BotFather |
| Telegram | `TELEGRAM_CHAT_ID` | Канал |
| Ollama | `OLLAMA_HOST` | Локально |
| OpenAI | `OPENAI_API_KEY` | platform.openai.com |
| MinIO | `MINIO_ROOT_USER` | Установка |
| MinIO | `MINIO_ROOT_PASSWORD` | Установка |

---

## Модели

| Модель | Использование | Установка |
|--------|--------------|-----------|
| kimi-k2.6:cloud | Основная (default) | `ollama pull` |
| gpt-4o | Альтернатива | API ключ |
| claude-sonnet | Альтернатива | API ключ |
| all-MiniLM-L6-v2 | Embeddings | `pip install sentence-transformers` |

---

## Порты

| Порт | Сервис |
|------|--------|
| 8443 | OpenClaw Office UI |
| 3456 | AI Office Dashboard |
| 9000 | MinIO API |
| 9001 | MinIO Console |
| 8080 | SearXNG |
| 11434 | Ollama |

---

## Устранение неполадок

### Модель не отвечает
```bash
ollama ps  # проверить запущенные модели
ollama pull kimi-k2.6:cloud  # переустановить
```

### MinIO не доступен
```bash
docker logs minio
docker restart minio
```

### Telegram не отправляет
```bash
curl "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getMe"
# Должен вернуть JSON с info о боте
```

### Скиллы не найдены
```bash
ls /opt/openclaw-stack/workspace/skills/ | wc -l
# Должно быть 100+
```

---

## Готово!

**Dashboard:** http://YOUR_SERVER:3456
**S3:** http://YOUR_SERVER:9000 (minio/minio123)
**OpenClaw UI:** http://YOUR_SERVER:8443
**GitHub:** https://github.com/sidnevart/chappi-ai-office-v2
