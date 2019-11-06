from mongoengine import DynamicDocument, EmbeddedDocument, fields


class DocumentMixin:
    @classmethod
    def UpdateOne(cls, instance):
        item = cls.objects(ID=instance.id).first()

        if item is None:
            cls.from_instance(instance).save()
        else:
            it = cls.from_instance(instance)
            it.id = item.id
            it.save()

    @classmethod
    def from_instance(cls, instance):
        pass
