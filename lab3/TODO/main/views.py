import json

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


class TodoList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'todo_list.html'

    def get(self, request, pk, *args, **kwargs):
        mock_file = open('static/mock/mock_list.json')

        todo_list = filter(lambda list_item: not list_item['completed'],
                           json.load(mock_file))
        return Response({'todo_list': todo_list, 'list_id': pk})


class TodoCompletedList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'completed_todo_list.html'

    def get(self, request, pk, *args, **kwargs):
        mock_file = open('static/mock/mock_list.json')

        todo_list = filter(lambda list_item: list_item['completed'],
                           json.load(mock_file))
        return Response({'todo_list': todo_list, 'list_id': pk})