from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from task_manager.labels.forms import AddLabelForm
from task_manager.labels.models import Label
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserNotAuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, "Вы не авторизованы! Пожалуйста, выполните вход."
            )
        return super().dispatch(request, *args, **kwargs)


class AddLabel(UserNotAuthenticatedMixin, SuccessMessageMixin, CreateView):
    form_class = AddLabelForm
    template_name = 'label/label_form.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно создана'
    extra_context = {
        'title': 'Создать метку',
        'button_name': 'Создать'
    }


class UpdateLabel(UserNotAuthenticatedMixin, UpdateView):
    model = Label
    form_class = AddLabelForm
    template_name = 'label/label_form.html'
    success_url = reverse_lazy('labels_list')
    success_message = 'Метка успешно изменена'
    extra_context = {
        'title': 'Изменение метки',
        'button_name': 'Изменить'
    }


class DeleteLabel(UserNotAuthenticatedMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'label/label_form.html'
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
    template_name = 'label/label_list.html'
    context_object_name = 'labels'
