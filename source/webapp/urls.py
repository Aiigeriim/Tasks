# from django.urls import path
#
# from webapp.views import update_task, delete_task, delete_all_tasks, IndexView, CreateTaskView, \
#     DetailTaskView
#
# urlpatterns = [
#     path('', IndexView.as_view(), name='index'),
#     path('add-task/', CreateTaskView.as_view(), name='create_task'),
#     path('task/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
#     path('task/<int:pk>/update/', update_task, name='update_task'),
#     path('task/<int:pk>/delete/', delete_task, name='delete_task'),
#     path('tasks/delete/', delete_all_tasks, name='delete_all_tasks'),
#
# ]