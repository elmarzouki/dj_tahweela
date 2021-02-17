dj_tahweela
===========

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy dj_tahweela

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd dj_tahweela
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



Run & go
--------
PLEASE NOTE: I kept the .env/* and credentials as plain for easier reviewing.
Build and Run the app using docker.
```bash
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up

$ docker-compose -f local.yml run django python manage.py makemigrations
$ docker-compose -f local.yml run django python manage.py migrate
$ firefox http://localhost:8000/
```
Django shell: `docker-compose -f local.yml run --rm django python manage.py shell_plus `
Logs: `docker-compose -f local.yml logs`
Unittests: `$ docker-compose -f local.yml run django python manage.py test`


API
^^^
Please, Check Postman collection. But for quick examples:
1. POST http://localhost:8000/auth-token/
   body```json  {"username": "elmarzouki", "password": "elmarzouki"}```
   response {"token": "32b48b9816a0ea7d12c32af9b6153210cc8c17c7"}

2. GET http://localhost:8000/api/users/me/
   headers Authorization = TOKEN 32b48b9816a0ea7d12c32af9b6153210cc8c17c7
   response logged user data

3. GET http://localhost:8000/api/currencies/status/
   response {"Status": "Currencies App Up!"}