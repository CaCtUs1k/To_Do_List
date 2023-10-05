from django.urls import path

from main.views import TaskListView, TaskCreateView, TaskUpdateView, toggle_task_status, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle-status/",
        toggle_task_status,
        name="toggle-status"
    ),
]

app_name = "main"
