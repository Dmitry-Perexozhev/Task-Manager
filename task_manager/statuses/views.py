from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from task_manager.statuses.forms import AddStatusForm
from task_manager.statuses.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect


class AddStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AddStatusForm
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно создан'
    extra_context = {
        'title': 'Создать статус',
        'button_name': 'Создать'
    }


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = AddStatusForm
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Пользователь успешно изменен'
    extra_context = {
        'title': 'Изменение статуса',
        'button_name': 'Изменить'
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class DeleteStatus(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно удален'
    extra_context = {
        'title': 'Удаление статуса',
        'button_name': 'Да, удалить',
        'is_delete_view': True
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Невозможно удалить статус, потому что он используется")
            return redirect(self.success_url)


class ListStatuses(LoginRequiredMixin, ListView):
    model = Status
    fields = ['id', 'name', 'created_at']
    ordering = ['id']
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)
