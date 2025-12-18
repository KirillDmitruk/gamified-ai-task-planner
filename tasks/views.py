from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks.models import Task


class TaskCreateView(CreateView):
    model = Task


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
