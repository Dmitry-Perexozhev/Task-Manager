from django.urls import reverse_lazy
from task_manager.tasks.forms import AddTaskForm
from task_manager.tasks.models import Task
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserNotAuthenticatedMixin, UserIsOwnerMixin
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class ListTasks(UserNotAuthenticatedMixin, FilterView):
    model = Task
    fields = '__all__'
    ordering = ['id']
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_queryset(self):
        queryset = Task.objects.all()
        only_my_tasks = self.request.GET.get('current_user', False)
        if only_my_tasks:
            queryset = queryset.filter(author=self.request.user)
        return queryset


class AddTask(UserNotAuthenticatedMixin, SuccessMessageMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно создана'
    extra_context = {
        'title': 'Создать задачу',
        'button_name': 'Создать'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(UserNotAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно изменена'
    extra_context = {
        'title': 'Изменение задачи',
        'button_name': 'Изменить'
    }


class DeleteTask(UserNotAuthenticatedMixin, UserIsOwnerMixin,
                 SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно удалена'
    message_error = "Задачу может удалить только ее автор"
    extra_context = {
        'title': 'Удаление задачи',
        'button_name': 'Да, удалить',
        'is_delete_view': True
    }


class TaskView(UserNotAuthenticatedMixin, DetailView):
    model = Task
    template_name = 'task/task_view.html'
    context_object_name = 'task'
