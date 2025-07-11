from django.urls import path

from webapp.views import delete_all_tasks, IndexView, CreateTaskView, \
    DetailTaskView, UpdateTaskView, DeleteTaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-task/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('tasks/delete/', delete_all_tasks, name='delete_all_tasks'),

]