from django import forms

from task_manager.labels.models import Label


class AddLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Имя'
        }
