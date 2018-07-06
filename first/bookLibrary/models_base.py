from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """基础类，抽象类，大多数模型都能用到"""
    create_date = models.DateTimeField(auto_created=True, help_text='创建时间')
    modify_date = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    is_delete = models.BooleanField(default=False, help_text='是否删除，默认为否')
    is_discard = models.BooleanField(default=False, help_text='是否废弃，默认为否')
    order = models.IntegerField(default=99, help_text='排序')

    class Meta:
        abstract = True


class NotDeleteManager(models.Manager):
    """获取未删除的对象"""

    def get_queryset(self):
        return super(NotDeleteManager, self).get_queryset().filter(is_delete=False)
