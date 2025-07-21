from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class TaskStatus(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.name[:20]


    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = "Статусы"