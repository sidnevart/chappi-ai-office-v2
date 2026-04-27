# План: Система Research для OpenClaw

## Цель
Построить автоматизированную research-систему внутри OpenClaw, которая самостоятельно (или по запросу) исследует рынки, компании, тренды, генерирует идеи B2B/B2C, создаёт pitch-презентации и артефакты.

---

## Фаза 1: Инфраструктура и Агенты (Неделя 1)

### 1.1 Агенты (специализация)

| Агент | Роль | Триггер |
|-------|------|---------|
| **Research Lead** | Оркестратор, декомпозиция задач, планирование | Запрос пользователя |
| **Web Researcher** | Поиск в интернете, скрейпинг, сбор данных | Задание от Lead |
| **Company Analyst** | Глубокий анализ компании, продукты, конкуренты | Задание от Lead |
| **Idea Generator** | Генерация идей, поиск слабых мест, креатив | Данные от Analyst |
| **Financial Analyst** | Финансовые расчёты, модели, юнит-экономика | Идея от Generator |
| **Pitch Creator** | Создание презентаций (HTML/Google Slides) | Финальная идея |
| **Tracker** | Мониторинг фондов, грантов, программ (фоновый) | Cron ежедневно |

### 1.2 Инструменты (Composio + OpenClaw)

| Инструмент | Назначение | Статус |
|-----------|-----------|--------|
| Browser Tool (Composio) | Автоматический веб-браузер, скрейпинг | ✅ Готов |
| Web Search (Composio) | Поиск, новости, аналитика | ✅ Готов |
| Google Sheets | Таблицы, расчёты, хранение данных | ✅ Подключен |
| Google Docs | Документы, отчёты | ✅ Подключен |
| Google Drive | Хранилище артефактов | ✅ Подключен |
| Telegram Bot | Уведомления, доставка результатов | ✅ Готов |
| HTML Generator | Локальные pitch-презентации | ✅ (workbench) |

### 1.3 Хранилище данных

**Структура артефактов:**
```
/opt/openclaw-stack/workspace/research/
├── companies/           # Данные по компаниям
│   ├── {company_name}/
│   │   ├── profile.json
│   │   ├── products.md
│   │   ├── competitors.md
│   │   └── analysis.md
├── ideas/               # Сгенерированные идеи
│   ├── {idea_id}/
│   │   ├── pitch.html
│   │   ├── financial_model.gsheet
│   │   ├── analysis.md
│   │   └── sources/
├── market_research/      # Рыночные отчёты
├── opportunities/        # Гранты, школы, фонды
│   ├── grants/
│   ├── accelerators/
│   ├── summer_schools/
│   └── vc_funds/
└── templates/            # Шаблоны презентаций
```

**Google Sheets:**
- `Research Pipeline` — очередь задач
- `Company Database` — справочник компаний
- `Idea Tracker` — идеи со статусами
- `Financial Models` — расчёты
- `Opportunities Tracker` — гранты, школы, фонды

---

## Фаза 2: Ресурсы для мониторинга (Неделя 1-2)

### 2.1 Фонды и инвесторы

**Топ фонды (трекинг):**
1. Sequoia Capital
2. Andreessen Horowitz (a16z)
3. Y Combinator
4. Founders Fund
5. Lightspeed Venture Partners
6. Bessemer Venture Partners
7. Index Ventures
8. Accel
9. Khosla Ventures
10. Greylock Partners

**Источники данных:**
- Crunchbase (API/скрейпинг)
- PitchBook (данные)
- VC фонды blogs/portfolios
- Twitter/X фондов

### 2.2 Гранты и программы

**Грантовые программы:**
| Программа | Тип | Сумма | Трекинг |
|-----------|-----|-------|---------|
| NSF SBIR/STTR | USA | до $2M | Ежемесячно |
| NIH Grants | USA | варьируется | Ежемесячно |
| EU Horizon | Europe | до €10M | Ежемесячно |
| Y Combinator | Global | $500K | Постоянно |
| Techstars | Global | $120K | Постоянно |
| 500 Startups | Global | $150K | Постоянно |

**Университетские программы:**
- Stanford OVAL
- MIT Sandbox
- Harvard Innovation Labs
- Berkeley SkyDeck
- Oxford Foundry
- ETH Pioneer Fellowship

**Летние школы / буткемпы:**
- founders.inc
- Pioneer
- Stellar Formation
- Buildspace

### 2.3 Telegram каналы (работа)

**Зарубеж:**
- @remoteitjobs
- @devsjob
- @remote_hacker

**Россия/СНГ:**
- @fordev
- @devops_jobs
- @python_jobs

---

## Фаза 3: Скиллы (Неделя 2)

### 3.1 Skill: `deep-research`

**Вход:** URL или запрос (query)
**Выход:** Структурированный отчёт (JSON + Markdown)

**Алгоритм:**
1. Поиск через Web Search (3-5 запросов)
2. Fetch контента с топ-10 страниц
3. Извлечение: компания, продукты, конкуренты, фондирование, команда
4. Сохранение в `companies/{name}/profile.json`

### 3.2 Skill: `company-analysis`

**Вход:** Название компании
**Выход:** Полный анализ (Markdown)

**Алгоритм:**
1. Загрузка профиля из кеша / research
2. Анализ продуктовой линейки
3. Поиск конкурентов (direct + indirect)
4. SWOT-анализ
5. Слабые места = возможности
6. Рекомендации

### 3.3 Skill: `idea-generator`

**Вход:** Анализ компании или тренд
**Выход:** Список идей с оценкой

**Алгоритм:**
1. Анализ проблем клиентов (reviews, forums)
2. Сравнение с конкурентами (feature gaps)
3. Brainstorm решений
4. Фильтрация по критериям:
   - Размер рынка (TAM/SAM/SOM)
   - Сложность реализации
   - Конкурентное преимущество
   - Время до MVP
5. Ранжирование

### 3.4 Skill: `financial-model`

**Вход:** Идея B2B/B2C
**Выход:** Google Sheet с моделью

**Структура:**
- Revenue assumptions (pricing, customers, growth)
- Cost structure (COGS, opex, team)
- Unit economics (CAC, LTV, payback)
- Cash flow (runway, break-even)
- Sensitivity analysis

### 3.5 Skill: `pitch-deck`

**Вход:** Идея + финансовая модель
**Выход:** HTML презентация

**Структура:**
1. Title slide
2. Problem
3. Solution
4. Market
5. Product
6. Business Model
7. Traction
8. Competition
9. Financials
10. Team
11. Ask

### 3.6 Skill: `opportunity-tracker`

**Вход:** Тип (грант/акселератор/школа/фонд)
**Выход:** Обновлённый список возможностей

**Алгоритм:**
1. Поиск по заданным источникам
2. Извлечение: название, дедлайн, сумма, требования, ссылка
3. Сравнение с прошлым состоянием
4. Уведомление о новых / изменённых
5. Запись в Google Sheet

---

## Фаза 4: Cron задачи (фоновый мониторинг)

### Ежедневно (6:00 UTC)
```
cron: opportunity-tracker --type=grants
```
- Проверка грантовых программ
- Уведомление о новых

### Ежедневно (7:00 UTC)
```
cron: opportunity-tracker --type=accelerators
```
- Акселераторы и буткемпы

### Еженедельно (понедельник, 8:00 UTC)
```
cron: opportunity-tracker --type=funds
```
- Обзор активности фондов
- Новые инвестиции, тренды

### Еженедельно (вторник, 9:00 UTC)
```
cron: market-trends --sectors="physical AI,bioengineering,B2B SaaS,AI-native,crypto"
```
- Анализ трендов по секторам

### Ежедневно (10:00 UTC)
```
cron: telegram-job-scan --channels=remoteitjobs,devsjob,fordev
```
- Сканирование каналов на вакансии
- Фильтрация по ключевым словам

---

## Фаза 5: UI и взаимодействие (Неделя 3)

### 5.1 Grafana Dashboard: Research Overview

**Панели:**
- Активные research задачи
- Очередь идей (по статусу)
- Последние обновления по компаниям
- Гранты с дедлайнами (горящие)
- Финансовые модели (последние)
- Pitch decks (готовые)

### 5.2 Telegram интеграция

**Команды:**
- `/research {company}` — быстрый анализ
- `/idea` — сгенерировать идею
- `/pitch {idea_id}` — создать презентацию
- `/opportunities` — список возможностей
- `/track {company}` — добавить в мониторинг

### 5.3 Office UI

**Вкладки:**
- **Research Hub** — все задачи и их статус
- **Company Profiles** — карточки компаний
- **Idea Board** — Kanban досок идей
- **Financial Models** — ссылки на Google Sheets
- **Pitch Decks** — превью HTML презентаций
- **Opportunities** — календарь дедлайнов

---

## Фаза 6: Взаимодействие агентов (Неделя 3-4)

### 6.1 Механизм делегирования

```
Research Lead получает запрос
    ↓
Декомпозиция на подзадачи
    ↓
[Web Researcher] → собирает данные
    ↓
[Company Analyst] → анализирует
    ↓
[Idea Generator] → генерирует идеи
    ↓
[Financial Analyst] → считает модель
    ↓
[Pitch Creator] → делает презентацию
    ↓
Research Lead → финализирует, доставляет
```

### 6.2 Транспарентность

**Все действия логируются:**
- `/opt/openclaw-stack/workspace/research/logs/{task_id}/`
- Каждый агент пишет:
  - Что делал
  - Какие источники использовал
  - Промежуточные результаты
  - Почему принял то или иное решение

**UI:**
- Древовидная структура задач
- Раскрывающиеся детали по каждому шагу
- Ссылки на источники
- Время выполнения каждого шага

### 6.3 Shared State

**Файл:** `/opt/openclaw-stack/workspace/research/shared_state.json`

```json
{
  "active_tasks": [...],
  "company_profiles": {...},
  "ideas": {...},
  "opportunities": {...},
  "agent_status": {
    "research_lead": "idle",
    "web_researcher": "working_on:task_123",
    "company_analyst": "idle"
  }
}
```

---

## Первый шаг (сегодня)

1. ✅ Fallback модели убраны
2. 🔄 Создать структуру директорий research/
3. 🔄 Создать Google Sheets шаблоны
4. 🔄 Настроить cron задачи
5. 🔄 Создать первый skill (deep-research)
6. 🔄 Создать Grafana dashboard

**Ты готов начать? С чего начнём?**
