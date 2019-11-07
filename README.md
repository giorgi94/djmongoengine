# Django MongoEngine

This package, unlike [Django-MongoEngine](https://github.com/MongoEngine/django-mongoengine) or [Djongo](https://github.com/nesdis/djongo/), doesn't aim on changing SQL role in Django. Writing backend for NoSQL database is not trivial. Here MongoDB is used as helper database, to increase performance.


## Installation

To install the package by `pip` run following command

```sh
# From Github
$ pip install git+https://github.com/giorgi94/djmongoengine.git
```


## Usage

To start using the package, add `djmongoengine` to `INSTALLED_APPS` and define `MONGODB_DATABASES`


```python
# settings.py

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
        # "username": "user",
        # "password": "pass"
    },
}


```

Package provides mixin for document schema and connector

```python
# models.py

class DocumentMixin:
    @classmethod
    def UpdateOne(cls, instance):
        # updates document in MongoDB, which corresponeds to django instance

    @classmethod
    def from_instance(cls, instance):
        # create mongoengine document based on django instance

```

We assume that django `instance.id` is stored in `ID`, since `id` returns `_id` from mongodb. In the `example`, we provide basic example to define mongoengine schema, based on django models

```python
# myapp/models.py

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    alias = models.CharField(max_length=50)

# myapp/mongo.py

class Category(EmbeddedDocument):

    ID = fields.IntField()

    title = fields.StringField()
    alias = fields.StringField()

    @classmethod
    def from_instance(cls, instance):

        return cls(ID=instance.id, title=instance.title, alias=instance.alias)

```

In `signals.py` and `receivers.py` are defined functions and signals to sync changes in django to mongodb.

## GraphQL

GraphQL is not directly connected with the package, but documentation for `graphene` is not beginner friendly. There are [graphene-django](https://github.com/graphql-python/graphene-django) and [flask-graphql](https://github.com/graphql-python/flask-graphql), but it doesn't allow to explore full potential of `graphql` and `mongodb`, so we use [graphene-mongo](https://github.com/graphql-python/graphene-mongo) for more diversity. Query is defined in

```python
# myapp/query.py


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleQuery, find=FindInput())

    def resolve_articles(self, info, **kwargs):
        find = kwargs.get("find")

        normilize_find(find)

        if find is not None:
            return Article.objects(**find)
        return Article.objects()


schema = graphene.Schema(query=Query)

# myapp/views.py

from .query import schema


def graphql_view(request):
    ...

    result = schema.execute(query)

    if result.errors:
        return JsonResponse({"errors": str(result.errors)})

    return JsonResponse({"query": result.data})

```