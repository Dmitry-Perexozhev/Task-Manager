from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
    #     widget=forms.TextInput(
    #         attrs={
    #             # 'placeholder': 'Имя',
    #             # 'class': 'form-control'
    #         }
    #     )
    )
    last_name = forms.CharField(
        label='Фамилия',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Фамилия',
    #             'class': 'form-control'
    #         }
    #     )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Имя пользователя',
        # widget=forms.TextInput(
        #     attrs={
        #         'placeholder': 'Имя пользователя',
        #         'class': 'form-control'
        #     }
        # ),
        help_text='Обязательное поле. Не более 150 символов. '
                  'Только буквы, цифры и символы @/./+/-/_.'

    )
    password1 = forms.CharField(
        label='Пароль',
        # widget=forms.PasswordInput(
        #     attrs={
        #         'placeholder': 'Пароль',
        #         'class': 'form-control'
        #     }
        # ),
        help_text='Ваш пароль должен содержать как минимум 3 символа.'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        # widget=forms.PasswordInput(
        #     attrs={
        #         'placeholder': 'Подтверждение пароля',
        #         'class': 'form-control'
        #     }
        # ),
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.'
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        # widget=forms.TextInput(
        #     attrs={
        #         'placeholder': 'Имя пользователя',
        #         'class': 'form-control'
        #     }
        # )
    )
    password = forms.CharField(
        label="Пароль",
        # widget=forms.PasswordInput(
        #     attrs={
        #         'placeholder': 'Пароль',
        #         'class': 'form-control'
        #     }
        # )
    )

    class Meta:
        model = User
        fields = ['username', 'password']
