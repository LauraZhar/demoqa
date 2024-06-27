# Bookstore API и UI Автоматизированное Тестирование

## Описание проекта

Проект предназначен для автоматизированного тестирования Bookstore API и UI, включая регистрацию, авторизацию, добавление и удаление книг, а также получение информации о пользователях. Тесты написаны с использованием Page Object Model (POM), Pytest и Allure для генерации отчетов.

## Структура проекта

project_root/
├── pages/
│ ├── init.py
│ ├── base_page.py
│ ├── login_page.py
│ ├── register_page.py
│ └── books_page.py
├── tests/
│ ├── init.py
│ ├── test_ui.py
│ ├── test_api.py
├── config.py
├── conftest.py
├── pytest.ini
└── requirements.txt

perl
Копировать код

## Установка зависимостей

Убедитесь, что у вас установлен Python 3. Установите необходимые зависимости с помощью pip:

```bash
pip install -r requirements.txt
```
