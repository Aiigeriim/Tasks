from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'completion_date']
    list_display_links = ['id', 'name']
    list_filter = ['completion_date', 'status']
    search_fields = ['name']
    fields = ['name', 'status', 'completion_date', 'description' ]
    #readonly_fields = ['completion_date']


admin.site.register(Task, TaskAdmin)
