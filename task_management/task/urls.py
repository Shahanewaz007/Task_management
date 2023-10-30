from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.create_task, name='create_task'),
    path('task_list/', views.task_list, name='task_list'),
]