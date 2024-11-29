from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class UserNotAuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, "Вы не авторизованы! Пожалуйста, выполните вход."
            )
        return super().dispatch(request, *args, **kwargs)
