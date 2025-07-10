from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class BaseCreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    class Meta:
        abstract = True

class Task(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Задача')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    status = models.CharField(max_length=15, choices=status_choices, verbose_name='Статус', default='new')
    completion_date = models.DateField(auto_now=False, null=True, blank=True, verbose_name='Дэдлайн')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    # tags = models.ManyToManyField('webapp.Tag', related_name='tasks', verbose_name='Тэги', blank=True)
    tags = models.ManyToManyField(
        'webapp.Tag',
        related_name='tasks',
        verbose_name='Тэги',
        blank=True,
        through='webapp.TaskTag',
        through_fields=('task', 'tag')
    )
    def __str__(self):
        return f"{self.id} - {self.name}"


    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"


class Comment(BaseCreateUpdateModel):
   task = models.ForeignKey('webapp.Task', related_name='comments', on_delete=models.CASCADE, verbose_name='Задача')
   text = models.TextField(max_length=400, verbose_name='Комментарий')
   author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')


   def __str__(self):
       return self.text[:20]

   class Meta:
       db_table = 'comments'
       verbose_name = 'Комментарий'
       verbose_name_plural = "Комментарии"

class Tag(BaseCreateUpdateModel):
    name = models.CharField(max_length=50, verbose_name='Название', unique=True)
    # tasks = models.ManyToManyField('webapp.Task', related_name='tags', verbose_name='Задачи', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тэг'
        verbose_name_plural = "Тэги"


class TaskTag(BaseCreateUpdateModel):
    task = models.ForeignKey('webapp.Task', related_name='task_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey('webapp.Tag', related_name='tag_tasks', on_delete=models.CASCADE)