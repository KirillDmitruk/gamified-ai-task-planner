from django.urls import path
from tasks.apps import TasksConfig

app_name = TasksConfig.name

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/create/', TaskCreate.View.as_view(), name='task-create'),
    path('task/view/<pk>/', ..., name='task-view'),
    path('task/update/<pk>/', ..., name='task-update'),
    path('task/delete/<pk>/', ..., name='task-delete'),
    ]