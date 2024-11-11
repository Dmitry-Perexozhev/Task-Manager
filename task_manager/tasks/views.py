from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from task_manager.tasks.forms import AddTaskForm
from task_manager.tasks.models import Task
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            messages.error(request, "Задачу может удалить только ее автор")
            return redirect(request.META.get('HTTP_REFERER', reverse_lazy('tasks_list')))
        return super().dispatch(request, *args, **kwargs)


class ListTasks(LoginRequiredMixin, ListView):
    model = Task
    fields = '__all__'
    ordering = ['id']
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class AddTask(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно изменена'
    extra_context = {
        'title': 'Изменение задачи',
        'button_name': 'Изменить'
    }


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class DeleteTask(LoginRequiredMixin, UserIsOwnerMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task/task_form.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно удалена'
    extra_context = {
        'title': 'Удаление задачи',
        'button_name': 'Да, удалить',
        'is_delete_view': True
    }


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task/task_view.html'
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)