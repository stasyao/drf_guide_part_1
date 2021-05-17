# Учебный проект для пособия по djangorestframework

Запускаем проект на своей машине: 

1. Клонируем репозиторий `git clone https://github.com/stasyao/drf_guide_part_1`
2. Переходим в папку с проектом `cd drf_guide_part_1` (здесь и далее приводятся команды в bash-терминале на машине под win)
3. Устанавливаем виртуальное окружение `python -m venv env`
4. Запускаем виртуальное окружение `source env/Scripts/activate`
5. Устанавливаем в виртуальном окружении зависимости для проекта `pip install -r requirements.txt`
6. Делаем миграции для создания базы данных `python manage.py makemigrations && python manage.py migrate`
7. Заполняем данными таблицу Capital и таблицу auth.user `python manage.py loaddata db.json`
8. Запускаем локальный сервер `python manage.py runserver`
9. По адресу `http://localhost:8000` будет доступен список записей о столицах, a по адресу `http://localhost:8000/api/capitals` та же информация через API.
