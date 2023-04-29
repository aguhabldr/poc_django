# POC Django


## venv

## Start
        py -m venv venv
### deactivate
        deactivate


### Activate the virtual environment

    source venv/bin/activate

## Install python requirements

    pip3 install -r requirements.txt
    pip3 list

## Deactivate and reactivate virtual environment

    deactivate && source venv/bin/activate

## Run database migrations

    py manage.py migrate && python manage.py loaddata setup_groups

## Create superuser admin

    py manage.py createsuperuser

## To start the backend

    py manage.py runserver

## Start a new requirements.txt

    py -m pip freeze > requirements.txt