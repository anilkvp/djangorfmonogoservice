from django.db import models


# Create your models here.
class User(models.Model):
    _id = models.AutoField(primary_key=True, blank=False, serialize = False, verbose_name ='ID')
    username = models.CharField(max_length=200, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
