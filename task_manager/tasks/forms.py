from django import forms
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.user.models import User
from task_manager.labels.models import Label


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Имя',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Описание',
                    'cols': 40,
                    'rows': 10,
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'name': 'Имя',
            'description': 'Описание'
        }

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        empty_label='Статус не выбран',
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label='Исполнитель не выбран',
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label='Метки',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )
