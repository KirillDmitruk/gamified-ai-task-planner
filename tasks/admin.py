from django.contrib import admin

from tasks.models import Task, SubTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'description')
    search_fields = ('title',)
    list_filter = ('title', 'status')


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'task')
    search_fields = ('title',)
    list_filter = ('title', 'status')
