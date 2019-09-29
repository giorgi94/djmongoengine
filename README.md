# Django MongoEngine

This package, unlike [Django-MongoEngine](https://github.com/MongoEngine/django-mongoengine) or [Djongo](https://github.com/nesdis/djongo/), doesn't aim on changing SQL role in Django. Writing backend for NoSQL database is very


## Usage

```python

INSTALLED_APPS = [
    ...
    djmongoengine
    ...
]

MONGODB_DATABASES = {
    "default": {
        "name": "dbname",
        "host": '127.0.0.1',
        "port": 27017,
        "tz_aware": True,
    },
}


```