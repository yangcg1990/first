from django.db import models

from bookLibrary.models_base import BaseModel, NotDeleteManager


# Create your models here.
class Book(BaseModel):
    name = models.CharField(max_length=64, default='', help_text='书名')
    publish_date = models.CharField(max_length=64, default='', help_text='出版日期')
    author = models.ManyToManyField('Author', help_text='作者')

    objects = models.Manager
    notDeleteManager = NotDeleteManager()


class Author(BaseModel):
    name = models.CharField(max_length=32, default='', help_text='作者名字')
    age = models.IntegerField(default=0, help_text='作者年龄')
    sex = models.CharField(max_length=16, default='女', help_text='性别')

    objects = models.Manager
    notDeleteManager = NotDeleteManager()
