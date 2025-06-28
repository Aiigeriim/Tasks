from django.urls import path

from webapp.views import index, create_task, task_detail

urlpatterns = [
    path('', index, name='index'),
    path('add-task/', create_task, name='create_task'),
    path('task/<int:pk>', task_detail, name='task_detail'),
]


