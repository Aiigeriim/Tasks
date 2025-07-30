from django.db import models
from django.urls import reverse

from webapp.models import BaseCreateUpdateModel


class Project(BaseCreateUpdateModel):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name="Дэдлайн", null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"


    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = "Проекты"


    def get_absolute_url(self):
        return reverse('webapp:detail_project', kwargs={'pk': self.pk})
