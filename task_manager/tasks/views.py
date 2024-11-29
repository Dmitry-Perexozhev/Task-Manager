from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView
from task_manager.mixins import UserNotAuthenticatedMixin
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import AddTaskForm
from task_manager.tasks.models import Task


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            messages.error(
                request, "Задачу может удалить только ее автор"
            )
            return redirect(
                request.META.get('HTTP_REFERER', reverse_lazy('tasks_list'))
            )
        return super().dispatch(request, *args, **kwargs)


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
    template_name = 'task/create.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(UserNotAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/update.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно изменена'


class DeleteTask(UserNotAuthenticatedMixin, UserIsOwnerMixin,
                 SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно удалена'


class TaskView(UserNotAuthenticatedMixin, DetailView):
    model = Task
    template_name = 'task/task_view.html'
    context_object_name = 'task'
