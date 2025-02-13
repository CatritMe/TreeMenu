# Тестовое задание UpTrader

Это django app, который реализовывает древовидное меню.

## Функционал

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы.
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД


## Зависимости

Для управления зависимостями в проекте используется poetry.
Список зависимостей хранится в файле `pyproject.toml`
Установите все зависимости командой poetry install

## Установка

1. Клонируйте этот репозиторий на свой компьютер.
2. Установите необходимые зависимости с помощью `poetry install`.
3. Заполните файл `.env.example` и переименуйте его в `.env`.
4. В терминале выполните команду `python manage.py loaddata menu_data.json`
5. Запустите проект командой `python manage.py runserver`.


## Запуск через docker compose
Сборка и запуск контейнера в фоновом режиме:
docker-compose up -d --build
