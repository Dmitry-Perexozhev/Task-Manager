from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserNotAuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, "Вы не авторизованы! Пожалуйста, выполните вход."
            )
        return super().dispatch(request, *args, **kwargs)


class UserIsOwnerMixin:
    message_error = "У вас нет прав для изменения другого пользователя."
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(request, self.message_error)
            return redirect(reverse_lazy('users_list'))
        return super().dispatch(request, *args, **kwargs)
