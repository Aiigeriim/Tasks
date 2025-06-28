from django.urls import path

from webapp.views import index, create_task, task_detail

urlpatterns = [
    path('', index),
    path('add-task/', create_task),
    path('task/', task_detail)
]

