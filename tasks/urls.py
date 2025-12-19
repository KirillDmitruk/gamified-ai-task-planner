from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = TasksConfig.name

urlpatterns = [
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('', TaskListView.as_view(), name='task-list'),
    path('task/detail/<pk>/', TaskDetailView.as_view(), name='task-view'),
    path('task/update/<pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
