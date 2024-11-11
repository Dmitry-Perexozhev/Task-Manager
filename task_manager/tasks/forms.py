from django import forms

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.user.models import User


class AddTaskForm(forms.ModelForm):
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
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание', 'cols': 40, 'rows': 10, 'class': 'form-control'})
        }
        labels = {
            'name': 'Имя',
            'description': 'Описание'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"