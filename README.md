# Book Store Django Website

## Shortcut Commands

* Project

```bash
$ cd onedrive\desktop 
$ mkdir ch4-bookstore 
$ cd ch4-bookstore 
$ python -m venv .venv
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install django~=4.0.0 psycopg2-binary==2.9.3
(.venv) $ django-admin startproject django-project .
(.venv) $ python manage.py runserver
## Best Practice use Docker for Development
$ docker compose up -d --build
# Create User Model via docker
$ docker-compose exec web python manage.py startapp accounts
# Make migration via docker
$ docker-compose exec web python manage.py makemigrations accounts
# Make Superuser via docker
$ docker-compose exec web python manage.py createsuperuser
# Run test via docker
$ docker-compose exec web python manage.py test
```
