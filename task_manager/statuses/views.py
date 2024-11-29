from django.urls import reverse_lazy
from task_manager.mixins import UserNotAuthenticatedMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from task_manager.statuses.forms import AddStatusForm
from task_manager.statuses.models import Status
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect


class AddStatus(UserNotAuthenticatedMixin, SuccessMessageMixin, CreateView):
    form_class = AddStatusForm
    template_name = 'status/create.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно создан'


class UpdateStatus(UserNotAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = AddStatusForm
    template_name = 'status/update.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно изменен'


class DeleteStatus(UserNotAuthenticatedMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'status/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно удален'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, "Невозможно удалить статус, потому что он используется"
            )
            return redirect(self.success_url)


class ListStatuses(UserNotAuthenticatedMixin, ListView):
    model = Status
    fields = ['id', 'name', 'created_at']
    ordering = ['id']
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'
