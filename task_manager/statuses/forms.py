from django import forms
from task_manager.statuses.models import Status


class AddStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {
            'name': 'Имя'
        }
