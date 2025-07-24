from django.db import models
from django.db.models import RESTRICT
from django.urls import reverse

from webapp.models.base_create_update import BaseCreateUpdateModel


class Task(BaseCreateUpdateModel):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание', null=True, blank=True)
    status = models.ForeignKey('webapp.TaskStatus', related_name='statuses', on_delete=RESTRICT, verbose_name='Статус', default='new')
    type = models.ManyToManyField(
        'webapp.TaskType',
        related_name='tasks',
        verbose_name='Типы',
        blank=True,
        through='webapp.TaskTypeRelation',
        through_fields=('task', 'type')
    )
    def __str__(self):
        return f"{self.id} - {self.summary}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"


    def get_absolute_url(self):
        return reverse('webapp:detail_task', kwargs={'pk': self.pk})
