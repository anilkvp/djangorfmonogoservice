from mongoengine import Document, StringField


# Create your models here.
class User(Document):
    username = StringField(max_length=200, blank=False, default='')
    password = StringField(max_length=200, blank=False, default='')
