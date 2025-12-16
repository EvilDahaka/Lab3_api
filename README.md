# Лабораторна робота №3 — REST API веб-застосунок

## Опис проекту
Проєкт реалізує REST API та веб-інтерфейс для роботи з нотатками  
Використовується Flask та SQLite 
Архітектура:  
- **Контролери (controller)** — ендпоінти  
- **Сервіс (service)** — логіка  
- **Репозиторій (repository)** — доступ до БД

## Запуск проекту
1. Створити та активувати віртуальне середовище:

**Windows PowerShell:**
python -m venv venv
.\venv\Scripts\Activate.ps1

**Linux / macOS:**
python -m venv venv
source venv/bin/activate

2. Встановити Flask:
pip install flask

3. Запустити проект:
python app.py

Сервер запуститься на http://127.0.0.1:5000

- Веб-інтерфейс: `/notes`
- REST API: `/api/notes`
