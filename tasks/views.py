from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.services import create_task


class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        create_task(title=serializer.validated_data['title'], description=serializer.validated_data['description'],
                    user=self.request.user)


class TaskListView(ListView):
    model = Task

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Task List'
    #
    #     context['completed_count'] = Task.objects.filter(user=self.request.user, status='done').count()
    #
    #     context['in_progress'] = Task.objects.filter(user=self.request.user, status='in_progress').count()
    #
    #     return context
    # В шаблоне
    # <p>Выполнено: {{ completed_count }}</p>
    # <p>В процессе: {{ in_progress_count }}</p>


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
