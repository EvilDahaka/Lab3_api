# Лабораторна робота №3 — REST API веб-застосунок

## Опис проекту
Проєкт реалізує REST API та веб-інтерфейс для роботи з нотатками
Використовується Flask та SQLite 
Архітектура:
- **Контролери (controller)** — ендпоінти  
- **Сервіс (service)** — логіка  
- **Репозиторій (repository)** — доступ до БД

## Запуск проекту
1. Створити віртуальне середовище:

```
python -m venv venv
```

2. Активувати віртуальне середовище:

**Windows**
```
.\venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source venv/bin/activate
```

3. Встановити Flask:

```bash
pip install flask
```

4. Запустити проект:

```bash
python app.py
```

Сервер запуститься на http://127.0.0.1:5000

- Веб-інтерфейс: `/notes`
- REST API: `/api/notes`
