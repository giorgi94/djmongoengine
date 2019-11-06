from django.db.models import signals

from .models import Category, Article
from .receivers import set_alias, update_article_mongo, delete_article_mongo


signals.pre_save.connect(set_alias, Article)
signals.pre_save.connect(set_alias, Category)

signals.post_save.connect(update_article_mongo, Article)
signals.post_save.connect(update_article_mongo, Category)

signals.post_delete.connect(delete_article_mongo, Article)
signals.post_delete.connect(delete_article_mongo, Category)
