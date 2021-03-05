from django.contrib import admin

from . import models


@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ('name', 'owner', 'completed', 'list', 'created_at', 'due_date')
    list_display = ('name', 'owner', 'completed', 'list', 'created_at', 'due_date')
    search_fields = ['name', 'owner', 'completed', 'list', 'created_at', 'due_date']
