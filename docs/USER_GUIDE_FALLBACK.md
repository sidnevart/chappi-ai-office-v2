# Руководство: Управление fallback моделями через OpenClaw Dashboard

## Текущая конфигурация

**Primary model:** `ollama/kimi-k2.6:cloud`  
**Fallback models:** отключены (ручное управление)

---

## Как поменять модель вручную

### Способ 1: Через Control UI Dashboard

1. Открой: `https://80.74.25.43:8443/office/`
2. Найди секцию **Model** или **Agent Settings**
3. В поле **Primary Model** введи желаемую модель:
   - `ollama/kimi-k2.6:cloud` — основная модель (рекомендуется)
   - `ollama/kimi-k2.5:cloud` — запасная
   - `ollama/glm-5:cloud` — если нужна другая
   - `openai-codex/gpt-5.5` — через OpenAI API
4. Сохрани настройки
5. Gateway перезагрузит конфигурацию автоматически

### Способ 2: Через конфиг-файл (SSH)

```bash
# Открой конфиг
nano /root/.openclaw/openclaw.json
```

Найди секцию `agents.defaults.model`:

```json
"model": {
  "primary": "ollama/kimi-k2.6:cloud"
}
```

Для добавления fallback'ов (если понадобится):

```json
"model": {
  "primary": "ollama/kimi-k2.6:cloud",
  "fallbacks": [
    "ollama/kimi-k2.5:cloud"
  ]
}
```

Сохрани файл. Gateway применит изменения при следующем запросе.

### Способ 3: Через CLI (команда)

```bash
# Посмотреть текущую модель
openclaw config get agents.defaults.model.primary

# Установить модель
openclaw config set agents.defaults.model.primary "ollama/kimi-k2.6:cloud"

# Добавить fallback
openclaw config push agents.defaults.model.fallbacks "ollama/kimi-k2.5:cloud"

# Убрать все fallback'и
openclaw config set agents.defaults.model.fallbacks []
```

---

## Доступные модели в системе

| Модель | Провайдер | Контекст | Назначение |
|--------|-----------|----------|------------|
| `ollama/kimi-k2.6:cloud` | Ollama Cloud | 262k | Основная, универсальная |
| `ollama/kimi-k2.5:cloud` | Ollama Cloud | 200k | Запасная |
| `ollama/glm-5:cloud` | Ollama Cloud | 200k | Альтернатива |
| `openai-codex/gpt-5.5` | OpenAI | 200k | Coding tasks |
| `openai-codex/gpt-5.4` | OpenAI | 200k | Coding tasks (legacy) |

---

## Когда использовать fallback'ы

Fallback'ы полезны, когда:
- Primary модель временно недоступна (outage)
- Нужен другой контекстный размер
- Эксперименты с качеством ответов

**Но** — fallback'и добавляют непредсказуемость. Рекомендуется:
- Использовать **только primary** для стабильности
- Переключать модели **вручную** при необходимости
- Мониторить через Grafana dashboard

---

## Проверка текущей модели

```bash
openclaw status | grep -i model
```

Или в Grafana: **OpenClaw Usage Overview** → панель **Current Model**

---

## Мониторинг переключений

Если fallback'и включены, следи за алертом:
- `OpenClawGatewayRateLimited` — модель rate-limited
- `OpenClawGatewayProbeFailed` — gateway недоступен

В Grafana: **OpenClaw Health & Alerts** → **Rate Limit Recent**
