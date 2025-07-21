from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class TaskType(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return self.name[:20]


    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = "Типы"