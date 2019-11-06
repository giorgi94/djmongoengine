from mongoengine import fields, DynamicDocument, EmbeddedDocument

from djmongoengine.models import DocumentMixin


class Category(EmbeddedDocument):

    ID = fields.IntField()

    title = fields.StringField()
    alias = fields.StringField()

    @classmethod
    def from_instance(cls, instance):

        return cls(ID=instance.id, title=instance.title, alias=instance.alias)


class Article(DocumentMixin, DynamicDocument):
    meta = {"collection": "articles", "indexes": ["ID", "category.ID"]}

    ID = fields.IntField()

    title = fields.StringField()
    alias = fields.StringField()

    category = fields.EmbeddedDocumentField(Category, null=True)

    created = fields.DateTimeField(null=True)
    updated = fields.DateTimeField(null=True)

    @classmethod
    def from_instance(cls, instance):

        if instance.category is not None:
            category = Category.from_instance(instance.category)
        else:
            category = None

        return cls(
            ID=instance.id,
            title=instance.title,
            alias=instance.alias,
            created=instance.created,
            updated=instance.updated,
            category=category,
        )
