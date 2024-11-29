from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
    )
    last_name = forms.CharField(
        label='Фамилия',
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Имя пользователя',
        help_text='Обязательное поле. Не более 150 символов. '
                  'Только буквы, цифры и символы @/./+/-/_.'

    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(),
        help_text='Ваш пароль должен содержать как минимум 3 символа.'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password']
