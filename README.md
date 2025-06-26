# Diplom_3

## Дипломный проект. Задание 3: UI-тесты
<hr>

## Студент: Шаджанов Альберт

## <h>Когорта: #20

## <h>Project: Stellar Burgers</h>

Проект содержит автоматизированные тесты для веб-приложения "Stellar Burgers" с использованием:

Python + pytest как основного фреймворка

Selenium WebDriver для взаимодействия с браузером

Page Object Model (POM) для структурирования кода

Allure Framework для визуализации отчётов

Кроссбраузерное тестирование в Chrome и Firefox

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results
> 
Запуск с генерацией Allure-отчёта:
bash
pytest --alluredir=allure_results


Структура проекта:

stellar_burgers_tests/
│
├── pages/                  # Пакет с классами Page Object для каждой страницы
│   ├── base_page.py 
│   ├── forgot_password_page.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── order_feed_page.py
│   ├── password_reset_page.py
│   ├── profile_page.py
│   
│
├── tests/                  # Каталоги с тестами по функциональности
│   ├── test_main_page.py
│   ├── test_order_feed.py
│   ├── test_password_reset.py
│   └── test_profile.py
│
├── conftest.py             # Фикстуры для проекта
├── requirements.txt        # Зависимости проекта
├── README.md               # Документация проекта
└── curl.py                 # Urls для проекта
└── data.py                 # Тестовые данные для проекта



