from django.db import models

from webapp.models.base_create_update import BaseCreateUpdateModel


class TaskTypeRelation(BaseCreateUpdateModel):
    task = models.ForeignKey('webapp.Task', related_name='task_types', on_delete=models.CASCADE)
    type = models.ForeignKey('webapp.TaskType', related_name='type_tasks', on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'task_type_relations'
