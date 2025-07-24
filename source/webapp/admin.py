from django.contrib import admin
from webapp.models import Task, TaskStatus, TaskType


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id',  'created_at', 'summary', 'status', 'updated_at']
    list_display_links = ['id', 'summary']
    list_filter = ['status']
    search_fields = ['summary']
    fields = ['summary', 'status', 'description']



admin.site.register(Task, TaskAdmin)

class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ["id", 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    fields = ['name']


admin.site.register(TaskStatus, TaskStatusAdmin)

class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["id", 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    fields = ['name']

admin.site.register(TaskType, TaskTypeAdmin)
