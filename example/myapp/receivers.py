from django.template.defaultfilters import slugify
from unidecode import unidecode

from .mongo import Article as ArticleMongo, Category as CategoryMongo


def set_alias(sender, instance, **kwargs):
    alias = slugify(unidecode(instance.title))
    if alias != instance.alias:
        instance.alias = alias


def update_article_mongo(sender, instance, **kwargs):

    if sender.__name__ == "Article":
        ArticleMongo.UpdateOne(instance)
    elif sender.__name__ == "Category":
        category = CategoryMongo.from_instance(instance)
        ArticleMongo.objects(category__ID=instance.id).update(category=category)


def delete_article_mongo(sender, instance, **kwargs):

    if sender.__name__ == "Article":
        ArticleMongo.objects(ID=instance.id).delete()
    elif sender.__name__ == "Category":
        ArticleMongo.objects(category__ID=instance.id).update(category=None)
