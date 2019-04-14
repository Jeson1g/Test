from django.db import models


# Create your models here.
class List(models.Model):

    class Meta:
        db_table = 'tb_list'
        verbose_name = '待办事项清单'


class Item(models.Model):

    text = models.TextField()
    list = models.ForeignKey(List, default=None, blank=True)

    class Meta:
        db_table = 'tb_item'
        verbose_name = '待办事项'

