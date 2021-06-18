# Учебный проект для пособия по Django Rest Framework

Статьи на Хабре:
+ [Django Rest Framework для начинающих: создаём API для чтения данных (часть 1)](https://habr.com/ru/company/yandex_praktikum/blog/561696/)
+ [Django Rest Framework для начинающих: создаём API для чтения данных (часть 2)](https://habr.com/ru/company/yandex_praktikum/blog/562050/)

Запускаем проект на своей машине: 

1. Клонируем репозиторий `git clone https://github.com/stasyao/drf_guide_part_1`
2. Переходим в папку с проектом `cd drf_guide_part_1` (здесь и далее приводятся команды в bash-терминале на машине под win)
3. Устанавливаем виртуальное окружение `python -m venv env`
4. Запускаем виртуальное окружение `source env/Scripts/activate`
5. Обновляем pip `python -m pip install --upgrade pip`
6. Устанавливаем в виртуальном окружении зависимости для проекта `python -m pip install --no-cache-dir -r requirements.txt`
7. Делаем миграции для создания базы данных `python manage.py makemigrations && python manage.py migrate`
8. Заполняем данными модели `Capital` и `auth.user` &mdash; `python manage.py loaddata db.json`
9. Запускаем локальный сервер `python manage.py runserver`
10. По адресу `http://localhost:8000` будет доступен список записей о столицах, a по адресу `http://localhost:8000/api/capitals` та же информация через API.
