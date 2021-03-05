from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.TodoList.as_view()),
    path('<int:pk>/completed/', views.TodoCompletedList.as_view()),
]
