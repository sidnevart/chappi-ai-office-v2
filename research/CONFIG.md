# OpenClaw Research System - Configuration

## Google Sheets

| Назначение | URL | ID |
|-----------|-----|-----|
| Research Pipeline | https://docs.google.com/spreadsheets/d/1wq0DIpF4zmQSTSe9-eh0NpVKZrabEA7mkC4mi8OC3aA/edit | 1wq0DIpF4zmQSTSe9-eh0NpVKZrabEA7mkC4mi8OC3aA |
| Company Database | https://docs.google.com/spreadsheets/d/1MNFBoCTcJDqeTKGhT3BvAnVA_fu9lmDipXWXrVJ8yuo/edit | 1MNFBoCTcJDqeTKGhT3BvAnVA_fu9lmDipXWXrVJ8yuo |
| Idea Tracker | https://docs.google.com/spreadsheets/d/1IX3xj-tnuZqKLJIFmmedGJhVV3qKZAqhxly5PGMlnYo/edit | 1IX3xj-tnuZqKLJIFmmedGJhVV3qKZAqhxly5PGMlnYo |
| Financial Models | https://docs.google.com/spreadsheets/d/1y1g23Q9X5ASLCOUcBtVF679yC1cxwpWly63uNLah33o/edit | 1y1g23Q9X5ASLCOUcBtVF679yC1cxwpWly63uNLah33o |
| Opportunities Tracker | https://docs.google.com/spreadsheets/d/1SL5CgpDK3n2HE8yjjRvzHdWroEUgDfGFr0rB_AN67zM/edit | 1SL5CgpDK3n2HE8yjjRvzHdWroEUgDfGFr0rB_AN67zM |

## Директории

```
/opt/openclaw-stack/workspace/research/
├── companies/           # Профили компаний
├── ideas/               # Сгенерированные идеи
├── market_research/     # Рыночные отчёты
├── opportunities/       # Возможности
│   ├── grants/
│   ├── accelerators/
│   ├── summer_schools/
│   └── vc_funds/
├── templates/           # Шаблоны
├── scripts/             # Скрипты
└── logs/                # Логи
```

## Cron задачи

| Время | Задача | Описание |
|-------|--------|----------|
| 06:00 daily | grants | Мониторинг грантов |
| 07:00 daily | accelerators | Мониторинг акселераторов |
| 08:00 monday | funds | Обзор фондов |
| 09:00 tuesday | trends | Анализ трендов |
| 10:00 daily | jobs | Сканирование вакансий |

## Grafana Dashboards

- https://80.74.25.43:8443/grafana/d/openclaw-research
- https://80.74.25.43:8443/grafana/d/openclaw-memory
- https://80.74.25.43:8443/grafana/d/openclaw-health

## Telegram команды (планируемые)

| Команда | Описание |
|---------|----------|
| `/research {company}` | Быстрый анализ компании |
| `/idea` | Сгенерировать идею |
| `/pitch {idea_id}` | Создать презентацию |
| `/opportunities` | Список возможностей |
| `/track {company}` | Добавить в мониторинг |

## Модели (ручное управление)

**Primary:** `ollama/kimi-k2.6:cloud`  
**Fallback:** отключены

Для переключения: см. `/opt/openclaw-stack/workspace/docs/USER_GUIDE_FALLBACK.md`
