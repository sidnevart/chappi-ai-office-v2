# AI Office Research System — Декомпозированный план

## Домен 1: EDUCATION (Образование + Академические достижения)

### Skills

| Skill | Назначение | Вход | Выход |
|-------|-----------|------|-------|
| `edu_program_scout` | Поиск программ: буткемпы, летние школы, гранты | Фильтры (AI engineering, SWE, location) | Список программ с дедлайнами |
| `edu_competition_scout` | Поиск соревнований: Yandex Cup, ICSC, IAAC уровня | Направление, уровень | Список соревнований с призами |
| `edu_grant_scout` | Поиск грантов для студентов/проектов | Тема, сумма, location | Список грантов с требованиями |
| `edu_cv_matcher` | Сопоставление CV с требованиями программы | CV + описание программы | Score + gap analysis + рекомендации |
| `edu_application_builder` | Помощь в подготовке заявки | Программа + CV | Чек-лист, draft essays, портфолио-план |
| `edu_interview_prep` | Подготовка к интервью в программу | Программа + CV | Вопросы, план подготовки |

### Агенты

| Агент | Роль | Триггер | Коммуникация |
|-------|------|---------|------------|
| `EduBootcampScout` | Ищет буткемпы/летние школы по AI/SWE | Cron: ежедневно 09:00 | Пишет в `edu/bootcamps.json` |
| `EduCompetitionScout` | Ищет соревнования уровня Yandex Cup/ICSC/IAAC | Cron: ежедневно 09:00 | Пишет в `edu/competitions.json` |
| `EduGrantScout` | Ищет гранты для студентов и проектов | Cron: ежедневно 09:00 | Пишет в `edu/grants.json` |
| `EduOpportunityMatcher` | Сопоставляет CV с программами, ранжирует | Cron: еженедельно Пн 10:00 | Читает CV + все `.json`, пишет `edu/matched_opportunities.json` |
| `EduApplicationCoach` | Готовит заявки: чек-листы, драфты, таймлайны | Запрос пользователя | HTML-страница с планом подготовки |

---

## Домен 2: CAREER (Работа + Вакансии)

### Skills

| Skill | Назначение | Вход | Выход |
|-------|-----------|------|-------|
| `job_scout` | Поиск вакансий: AI Eng, Platform/DevOps, Backend | Фильтры (location, level, company) | Список вакансий с ссылками |
| `job_cv_matcher` | Сопоставление CV с JD | CV + job description | Score + gap analysis |
| `job_cover_letter` | Генерация сопроводительного письма | CV + JD + company | Готовое письмо |
| `job_interview_prep` | Подготовка к интервью | Company + role | Технические вопросы, поведенческие, план подготовки |
| `job_salary_research` | Исследование зарплат по рынку | Role + location + level | Диапазон, источники |
| `job_networking` | Поиск контактов, рефералов | Company + role | Список потенциальных контактов |

### Агенты

| Агент | Роль | Триггер | Коммуникация |
|-------|------|---------|------------|
| `JobScout` | Сканит вакансии AI Eng / Platform / Backend | Cron: ежедневно 09:00 | Пишет в `career/jobs.json` |
| `JobMatcher` | Ранжирует вакансии по соответствию CV | Cron: еженедельно Пн 10:00 | Читает CV + jobs, пишет `career/matched_jobs.json` |
| `JobApplicationBuilder` | Готовит заявку: CV tailoring, cover letter | Запрос пользователя | HTML-страница с пакетом документов |
| `JobInterviewCoach` | Готовит к интервью конкретной компании | Запрос пользователя | HTML-гайд |

---

## Домен 3: BUSINESS (Идеи + Компании + Финансы)

### Skills

| Skill | Назначение | Вход | Выход |
|-------|-----------|------|-------|
| `company_deep_dive` | Анализ компании: продукты, дочки, слабые места | Название компании | Полный профиль (JSON) |
| `competitive_analysis` | Конкуренты, positioning, дифференциация | Компания / идея | Отчёт |
| `market_trends` | Тренды: Physical AI, Bioengineering, B2B AI-native, Crypto | Сфера | Анализ тренда |
| `idea_generator` | Генерация и валидация идей | Проблема / тренд | Список идей с оценкой |
| `idea_strength_weakness` | Анализ слабых мест существующих решений | Продукт / сервис | Список недостатков + возможности |
| `financial_modeling` | Unit-economics, projections, Excel | Данные | Google Sheets |
| `pitch_builder` | HTML-презентация | Данные + шаблон | HTML файл |
| `tech_spec_writer` | Техническое задание | Продуктовое видение | ТЗ (Markdown/HTML) |
| `russian_market_analysis` | Анализ рынка РФ | Продукт / идея | Отчёт |
| `funding_scout` | Поиск инвестиций: фонды, акселераторы, гранты | Сфера + стадия | Список с контактами |
| `market_entry_strategy` | Стратегия выхода на рынок | Рынок + продукт | План |

### Агенты

| Агент | Роль | Триггер | Коммуникация |
|-------|------|---------|------------|
| `TrendMonitor` | Отслеживает тренды | Cron: ежедневно 09:00 | Пишет в `business/trends.json` |
| `DealFlowTracker` | Анализ последних инвестиций, фаунд-райзы | Cron: ежедневно 09:00 | Пишет в `business/deals.json` |
| `CompanyAnalyst` | Deep-dive на компанию | Запрос пользователя, Cron (топ из DealFlow) | Пишет в `business/companies/{name}.json` |
| `IdeaGenerator` | Генерирует идеи на основе трендов и проблем | Запрос пользователя, Cron | Пишет в `business/ideas.json` |
| `CompetitiveStrategist` | Анализирует: что предложить компании / как конкурировать | Запрос от `CompanyAnalyst` или `IdeaGenerator` | Пишет в `business/strategies.json` |
| `RussianMarketAnalyst` | Анализ рынка РФ | Запрос от `CompetitiveStrategist` | Пишет в `business/russian_market/{idea}.json` |
| `FundingScout` | Ищет инвестиции под идею | Запрос от `CompetitiveStrategist` | Пишет в `business/funding/{idea}.json` |
| `FinancialModeler` | Строит финансовую модель | Запрос от любого бизнес-агента | Google Sheets + отчёт |
| `PitchBuilder` | Создаёт HTML-презентацию | Запрос от любого бизнес-агента | HTML в `/office/pitches/` |
| `TechSpecWriter` | Пишет ТЗ для разработчиков | Запрос от `CompetitiveStrategist` | Markdown/HTML |

---

## SHARED Skills (для всех доменов)

| Skill | Назначение | Используют |
|-------|-----------|------------|
| `deep_research` | Базовый web research: search → fetch → synthesize | Все агенты |
| `browser_automation` | Скроллинг, динамический контент, rate limit management | CompanyAnalyst, скиллы с парсингом |
| `html_artifact_builder` | Создание HTML-артефактов в `/office/` | PitchBuilder, EduApplicationCoach, JobApplicationBuilder |
| `google_sheets_writer` | Запись данных в Google Sheets | FinancialModeler, все агенты с таблицами |
| `cv_parser` | Парсинг PDF CV, извлечение навыков/опыта | Все `*_cv_matcher` |

---

## Коммуникация между агентами

```
┌─────────────────────────────────────────────────────────────────┐
│                        SHARED STATE                             │
│  /mnt/files/research-state/                                     │
│  ├── edu/                                                       │
│  │   ├── bootcamps.json        ← EduBootcampScout               │
│  │   ├── competitions.json     ← EduCompetitionScout            │
│  │   ├── grants.json           ← EduGrantScout                  │
│  │   └── matched_opportunities.json ← EduOpportunityMatcher   │
│  ├── career/                                                    │
│  │   ├── jobs.json             ← JobScout                       │
│  │   └── matched_jobs.json     ← JobMatcher                     │
│  └── business/                                                  │
│      ├── trends.json           ← TrendMonitor                   │
│      ├── deals.json            ← DealFlowTracker                │
│      ├── companies/            ← CompanyAnalyst                 │
│      ├── ideas.json            ← IdeaGenerator                  │
│      ├── strategies.json       ← CompetitiveStrategist          │
│      ├── russian_market/       ← RussianMarketAnalyst           │
│      ├── funding/              ← FundingScout                   │
│      └── pitches/              ← PitchBuilder                   │
└─────────────────────────────────────────────────────────────────┘

Cron-триггеры (ежедневно 09:00):
  → EduBootcampScout
  → EduCompetitionScout
  → EduGrantScout
  → JobScout
  → TrendMonitor
  → DealFlowTracker

Cron-триггеры (еженедельно Пн 10:00):
  → EduOpportunityMatcher (CV + все edu/*.json → matched_opportunities)
  → JobMatcher (CV + jobs.json → matched_jobs)

Запрос пользователя (education):
  "Найди буткемпы по AI" → EduBootcampScout (inline, не cron)
  "Подготовь заявку в EEML" → EduApplicationCoach

Запрос пользователя (career):
  "Найди вакансии AI Engineer в London" → JobScout (inline)
  "Подготовь меня к интервью в Google" → JobInterviewCoach

Запрос пользователя (business):
  "Проанализируй CompanyX" 
    → CompanyAnalyst → business/companies/CompanyX.json
    → CompetitiveStrategist → business/strategies/CompanyX.json
    → (parallel) RussianMarketAnalyst → business/russian_market/CompanyX.json
    → (parallel) FundingScout → business/funding/CompanyX.json
    → (parallel) FinancialModeler → Google Sheets
    → PitchBuilder → /office/pitches/CompanyX.html
    → TechSpecWriter → /office/tech-specs/CompanyX.md

  "Придумай идею в Physical AI"
    → IdeaGenerator → business/ideas/physical_ai.json
    → CompetitiveStrategist → business/strategies/physical_ai.json
    → (parallel) RussianMarketAnalyst + FundingScout + FinancialModeler
    → PitchBuilder + TechSpecWriter

Прозрачность:
  Каждый агент пишет лог: research-log/YYYY-MM-DD/{agent_name}.json
  Видно в OpenClaw Office UI: статус, прогресс, артефакты
```

---

## Фаза 0: Инфраструктура (сейчас)

| Задача | Статус | Следующий шаг |
|--------|--------|---------------|
| Фикс EADDRINUSE | ✅ Готово | Проверить alert через 5-10 мин |
| Google Drive — забрать 3 CV из `cur_cv` | 🔄 Блокер | Подключить Google Drive |
| Создать структуру папок: `edu/`, `career/`, `business/` | ⏳ | После CV |

---

## Фаза 1: Фундамент (неделя 1)

| Домен | Что создаём | Артефакт |
|-------|------------|----------|
| **SHARED** | `deep_research` skill | `skills/deep-research/SKILL.md` |
| **SHARED** | `cv_parser` skill | `skills/cv-parser/SKILL.md` |
| **SHARED** | `html_artifact_builder` skill | `skills/html-builder/SKILL.md` |
| **EDU** | `edu_program_scout` skill | `skills/edu-program-scout/SKILL.md` |
| **EDU** | `edu_competition_scout` skill | `skills/edu-competition-scout/SKILL.md` |
| **EDU** | `edu_grant_scout` skill | `skills/edu-grant-scout/SKILL.md` |
| **EDU** | `EduBootcampScout` агент | Агент + cron |
| **EDU** | `EduCompetitionScout` агент | Агент + cron |
| **EDU** | `EduGrantScout` агент | Агент + cron |
| **CAREER** | `job_scout` skill | `skills/job-scout/SKILL.md` |
| **CAREER** | `JobScout` агент | Агент + cron |
| **BUSINESS** | `company_deep_dive` skill | `skills/company-deep-dive/SKILL.md` |
| **BUSINESS** | `market_trends` skill | `skills/market-trends/SKILL.md` |
| **BUSINESS** | `TrendMonitor` агент | Агент + cron |
| **BUSINESS** | `DealFlowTracker` агент | Агент + cron |

---

## Фаза 2: Аналитика (неделя 2)

| Домен | Что создаём |
|-------|------------|
| **EDU** | `edu_cv_matcher`, `edu_application_builder`, `edu_interview_prep` skills |
| **EDU** | `EduOpportunityMatcher`, `EduApplicationCoach` агенты |
| **CAREER** | `job_cv_matcher`, `job_cover_letter`, `job_interview_prep` skills |
| **CAREER** | `JobMatcher`, `JobApplicationBuilder`, `JobInterviewCoach` агенты |
| **BUSINESS** | `idea_generator`, `competitive_analysis`, `idea_strength_weakness` skills |
| **BUSINESS** | `CompanyAnalyst`, `IdeaGenerator`, `CompetitiveStrategist` агенты |
| **BUSINESS** | Browser automation для deep-dive |
| **SHARED** | `browser_automation` skill |

---

## Фаза 3: Продвинутый research (неделя 3-4)

| Домен | Что создаём |
|-------|------------|
| **EDU** | Программы уровня EEML, Stanford OVAL, NYIT-style грантов |
| **CAREER** | `job_salary_research`, `job_networking` skills |
| **CAREER** | Salary research, networking для AI/Platform/DevOps |
| **BUSINESS** | `russian_market_analysis`, `funding_scout`, `market_entry_strategy` skills |
| **BUSINESS** | `RussianMarketAnalyst`, `FundingScout` агенты |
| **BUSINESS** | `financial_modeling`, `pitch_builder`, `tech_spec_writer` skills |
| **BUSINESS** | `FinancialModeler`, `PitchBuilder`, `TechSpecWriter` агенты |
| **BUSINESS** | Full pipeline: компания → идея → стратегия → рынок РФ → финансы → питч → ТЗ |
| **SHARED** | `google_sheets_writer` skill |
| **SHARED** | Dashboard UI: активные агенты, прогресс, артефакты |
| **SHARED** | Прозрачность: лог мыслей агента, step-by-step |

---

## Фаза 4: Оптимизация (неделя 4+)

| Задача | Описание |
|--------|----------|
| Caching layer | Не дублируем research между доменами |
| Rate limit manager | Умное распределение запросов |
| Feedback loop | Ты оцениваешь → агенты улучшаются |
| Template library | 10+ HTML шаблонов под разные сценарии |
