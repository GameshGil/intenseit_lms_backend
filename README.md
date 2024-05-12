# intenseit_lms_backend


## Описание
Backend of LMS for Intense_IT


## Используемые технологии
- Python 3.11
- Django 5.0
- DRF 3.15
- DRF Simple JWT 5.3


## Авторы
Амиров Саид


## Запуск
- Необходимо клонировать проект на сервер.
- Перейти в папку проекта, создать и активировать виртуальное окружение для Python:
  - Создание виртуального окружения:

      ```python -m venv venv```

  - Активация виртуального окружения для Windows:

      ```source venv/Scripts/activate```

  - Активация виртуального окружения для Linux:

      ```source venv/bin/activate```

- Установить все требуемые для работы проекта библиотеки:

   ```pip install -r requirements.txt```

- Для создания базы данных в соответствии со структурой проекта в папке с файлом manage.py выполнить миграции:

   ```python manage.py migrate```

После выполнения подготовительных этапов проект готов к запуску. Рекомендуем предварительно создать суперпользователя для работы с админкой проекта.
- Для создания суперпользователя выполнить команду в терминале, подставив свои данные, и следовать последующим инструкциям:

   ```python manage.py createsuperuser --username='superuser' --email='superuser@mail.ru'```

Запуск проекта можно осуществить командой:

   ```python manage.py runserver```

После этого в браузере открыть страницу по адресу http://127.0.0.1:8000/. При переходе на странице отобразятся все доступные эндпоинты.
