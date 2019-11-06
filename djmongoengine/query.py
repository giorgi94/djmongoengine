import graphene
from graphene_mongo import MongoengineObjectType
from graphql_app.models import Article as ArticleModel
from graphql_app.models import Category as CategoryModel


class FindInput(graphene.InputObjectType):
    id = graphene.Int()


class Category(MongoengineObjectType):
    class Meta:
        model = CategoryModel


class Article(MongoengineObjectType):

    category = graphene.List(Category)

    class Meta:
        model = ArticleModel
        filter_fields = ["id"]


class Query(graphene.ObjectType):
    articles = graphene.List(Article, find=FindInput())

    def resolve_articles(self, info, **kwargs):
        find = kwargs.get("find")

        print(find)

        # if find is not None:
        #     return ArticleModel.objects(**find)
        return ArticleModel.objects()


schema = graphene.Schema(query=Query)

if __name__ == "__main__":

    query = """
        query {
            articles(find: { id: 80 }) {
                id
                title
            }
        }
    """

    result = schema.execute(query)

    # print(result.errors)
    # print(result.data)
