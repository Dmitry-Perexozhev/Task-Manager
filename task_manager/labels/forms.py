from django import forms
from task_manager.labels.models import Label


class AddLabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'})
        }
        labels = {
            'name': 'Имя'
        }