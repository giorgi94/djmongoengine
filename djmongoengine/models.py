
from mongoengine import Document, StringField, ListField, ReferenceField

class User(Document):
    meta = {'collection': 'users'}
    name = StringField()

class Page(Document):
    meta = {'collection': 'pages'}
    content = StringField()
    authors = ListField(ReferenceField(User))

'''
bob = User(name="Bob Jones").save()
john = User(name="John Smith").save()

Page(content="Test Page", authors=[bob, john]).save()
Page(content="Another Page", authors=[john]).save()
'''