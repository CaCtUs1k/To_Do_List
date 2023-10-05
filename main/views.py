from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from main.forms import TaskForm
from main.models import Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "main/task_list.html"
    paginate_by = 5
    queryset = Task.objects.all()


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("main:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("main:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("main:task-list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return redirect("main:task-list")
