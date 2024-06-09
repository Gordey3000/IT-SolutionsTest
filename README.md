## Проект API для It-Solutions
### Описание:
Проект работает на Django Rest Fraemwork

### В API доступны следующие эндпоинты:
http://127.0.0.1:8000/api/v1/ads/ При GET-запросе на этот эндпоинт будет получен список объявлений ( выдача будет осуществляться с пагинацией).
Пример запроса страницы 2:
```
http://127.0.0.1:8000/api/v1/ads/?page=2
```

http://127.0.0.1:8000/api/v1/ads/{id}/ GET-запрос позволяет поучить объявление по id.


http://127.0.0.1:8000/api/v1/register/ При Post-запросе будет выполнена регистрация пользователя и получения токена.
Пример запроса
```
{
    "username": "example_user",
    "password": "securepassword",
    "email": "example@example.com"
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gordey3000/IT-SolutionsTest
```

```
cd IT-SolutionsTest
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install -U pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
python manage.py makemigrations
```

Заполнить базу данных:

```
python scraper.py
```

Запустить проект:

```
python manage.py runserver
```
