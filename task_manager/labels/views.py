from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.labels.forms import AddLabelForm
from task_manager.labels.models import Label
from task_manager.mixins import UserNotAuthenticatedMixin


class AddLabel(UserNotAuthenticatedMixin, SuccessMessageMixin, CreateView):
    form_class = AddLabelForm
    template_name = 'label/create.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно создана'


class UpdateLabel(UserNotAuthenticatedMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = AddLabelForm
    template_name = 'label/update.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно изменена'


class DeleteLabel(UserNotAuthenticatedMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/delete.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно удалена'
    extra_context = {
        'title': 'Удаление метки',
        'button_name': 'Да, удалить',
        'is_delete_view': True
    }

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.task_set.exists():
            messages.error(
                request, "Невозможно удалить метку, потому что она используется"
            )
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)


class ListLabels(UserNotAuthenticatedMixin, ListView):
    model = Label
    fields = ['id', 'name', 'created_at']
    ordering = ['id']
    template_name = 'label/labels_list.html'
    context_object_name = 'labels'
