from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name='Задача')
    status = models.CharField(max_length=15, choices=status_choices, default='new')
    completion_date = models.DateField(auto_now=False, verbose_name='Дата выполнения')


    def __str__(self):
        return f"{self.id} - {self.name}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"

