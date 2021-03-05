import json

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from . import models


class TodoList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request, pk, *args, **kwargs):
        todo_list = models.Task.objects.filter(list__id=pk, completed=False)
        return Response({'todo_list': todo_list, 'list_id': pk})


class TodoCompletedList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'completed_todo_list.html'

    def get(self, request, pk, *args, **kwargs):
        todo_list = models.Task.objects.filter(list__id=pk, completed=True)
        return Response({'todo_list': todo_list, 'list_id': pk})
