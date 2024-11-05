from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from task_manager.user.forms import RegisterUserForm, LoginUserForm
from task_manager.user.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != request.user:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect(reverse_lazy('users_list'))
        return super().dispatch(request, *args, **kwargs)


class AddUser(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('login_user')
    success_message = 'Пользователь успешно зарегистрирован'
    extra_context = {
        'title': 'Регистрация',
        'button_name': 'Зарегистрировать'
    }


class UpdateUser(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно изменен'
    extra_context = {
        'title': 'Изменение пользователя',
        'button_name': 'Изменить'
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class DeleteUser(SuccessMessageMixin, LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = User
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('home')
    success_message = 'Пользователь успешно удален'
    extra_context = {
        'title': 'Удаление пользователя',
        'button_name': 'Да, удалить',
        'is_delete_view': True
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
        return super().dispatch(request, *args, **kwargs)


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'
    extra_context = {
        'title': 'Вход',
        'button_name': 'Войти'
    }

    def form_invalid(self, form):
        form.errors.clear()
        messages.error(self.request, "Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.")
        return super().form_invalid(form)


class LogoutUser(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)


class ListUsers(ListView):
    model = User
    fields = ['id', 'username', 'first_name', 'last_name', 'created_at']
    ordering = ['id']
    template_name = 'user/users_list.html'
    context_object_name = 'users'