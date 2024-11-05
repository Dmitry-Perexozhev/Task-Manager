from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from task_manager.statuses.forms import AddStatusForm
from task_manager.statuses.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class AddStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AddStatusForm
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно создан'
    extra_context = {
        'title': 'Создать статус',
        'button_name': 'Создать'
    }


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


class ListStatuses(LoginRequiredMixin, ListView):
    model = Status
    fields = ['id', 'name', 'created_at']
    ordering = ['id']
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'