from django.db import models
from django.db.models import RESTRICT


class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


    class Meta:
        abstract = True


class Task(BaseCreateUpdateModel):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    status = models.ForeignKey('webapp.TaskStatus', related_name='statuses', on_delete=RESTRICT, verbose_name='Статус', default='new')
    type = models.ForeignKey('webapp.TaskType', related_name='types', on_delete=RESTRICT, verbose_name='Тип')

    def __str__(self):
        return f"{self.id} - {self.summary}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"


class TaskType(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return self.name[:20]


    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = "Типы"


class TaskStatus(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.name[:20]


    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = "Статусы"



