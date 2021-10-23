# cloudsek-task

Setup

1) install postgresql
2) install pgadmin4
3) Setup Virtual Environment
    pip install virtualenvwrapper-win
    mkvirtuallenv 'name of your Environment'
    eg: mkvirtuallenv test
    to open Virtual Environment
    use command "workon test"

Project Setup

1) Download Dependencies
    pip install -r requirements.txt

2) Setup postgresql - inside pgadmin4 application
    create new database as "cloudsekdatabase" with user as "postgres" and password = "1234"
    You will be prompted for a password.

Running Project

1) Migrations
    python manage.py migrate

2) Running the server
    python manage.py runserver
