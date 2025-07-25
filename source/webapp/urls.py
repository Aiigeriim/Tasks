from django.urls import path
from webapp.views import TaskListView, CreateTaskView, DetailTaskView, UpdateTaskView, DeleteTaskView, DeleteAllTasksView

app_name = 'webapp'


urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('add-task/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('tasks/delete/', DeleteAllTasksView.as_view(), name='delete_all_tasks'),

]