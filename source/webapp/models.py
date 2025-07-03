from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name='Задача')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    status = models.CharField(max_length=15, choices=status_choices, default='new')
    completion_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name='Дэдлайн')


    def __str__(self):
        return f"{self.id} - {self.name}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"
