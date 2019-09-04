# Python TreinaWeb
Simple repository to enjoy the week of the Python and Django with TreinaWeb.
To know more details follow this link: https://lp.treinaweb.com.br/python

## Create virtualenv
 Creating the virtual environment for this project:
```sh
$ python -m venv python_treinaweb_venv
```

## Activate virtualenv
```sh
$ source python_treinaweb_venv/bin/activate # Linux or macOS
$ source python_treinaweb_venv/Scripts/activate # Windows
```

## Disable virtualenv
To disable the virtualenv just run:
```sh
$ deactivate
```

## Install Django
This will install Django on your virtualenv:
```sh
$ pip install Django==2.2.4
```

## Create the project and app
With Django installed, follow this commands:
```sh
$ django-admin startproject task_manager
$ python manage.py startapp app
```

## Run the server
```sh
$ cd task_manager
$ python manager.py runserver
```