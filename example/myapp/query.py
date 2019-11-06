import graphene
from graphene_mongo import MongoengineObjectType

from .mongo import Category, Article


def normilize_find(find):

    for key, val in find.items():
        if key == "cID":
            find["category__ID"] = find.pop("cID")


class FindInput(graphene.InputObjectType):
    ID = graphene.Int()
    cID = graphene.Int()


class CategoryQuery(MongoengineObjectType):
    class Meta:
        model = Category


class ArticleQuery(MongoengineObjectType):

    category = graphene.Field(CategoryQuery)

    class Meta:
        model = Article


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleQuery, find=FindInput())

    def resolve_articles(self, info, **kwargs):
        find = kwargs.get("find")

        normilize_find(find)

        if find is not None:
            return Article.objects(**find)
        return Article.objects()


schema = graphene.Schema(query=Query)
