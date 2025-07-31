from django.urls import path
from webapp.views import TaskListView, CreateTaskView, DetailTaskView, UpdateTaskView, DeleteTaskView, DeleteAllTasksView
from webapp.views.projects import ProjectListView, DetailProjectView, CreateProjectView, UpdateProjectView, \
    DeleteProjectView

app_name = 'webapp'


urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('project/<int:pk>/detail', DetailProjectView.as_view(), name='detail_project'),
    path('add-project/', CreateProjectView.as_view(), name='create_project'),
    path('project/<int:pk>/update/', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', DeleteProjectView.as_view(), name='delete_project'),



    path('tasks/', TaskListView.as_view(), name='index'),
    path('add-task/', CreateTaskView.as_view(), name='create_task'),
    path('task/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
    path('tasks/delete/', DeleteAllTasksView.as_view(), name='delete_all_tasks'),

]