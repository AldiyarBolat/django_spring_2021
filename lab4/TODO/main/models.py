import datetime

from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    due_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=5))
