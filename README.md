Fast Api Blog
Source: https://blog.yezz.me/blog/Build-and-Secure-an-API-in-Python-with-FastAPI

## Quickstart

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    cp .env.example .env

To run the web application::

    make run_local

## Run tests

    $ pytest
    ================================================= test session starts ==================================================
    $

If you want to run a specific test, you can do this with `this
$ pytest tests/test_api/test_routes/test_users.py::test_user_can_not_take_already_used_credentials

## Web routes

## Project structure

```sh
├── Makefile
├── README.md
├── __init__.py
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── blog.py
│   │   └── user.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── blog.py
│   │   ├── configs.py
│   │   ├── settings
│   │   │   ├── __init__.py
│   │   │   ├── app.py
│   │   │   ├── development.py
│   │   │   ├── production.py
│   │   │   └── test.py
│   │   └── user.py
│   ├── database
│   │   └── configuration.py
│   ├── main.py
│   ├── models
│   │   └── models.py
│   ├── schema
│   │   ├── hash.py
│   │   ├── oauth2.py
│   │   ├── schemas.py
│   │   └── token.py
│   └── test_main.py
├── blog.db
├── curl.txt
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── static
    └── bird-thumbnail.jpeg
```
