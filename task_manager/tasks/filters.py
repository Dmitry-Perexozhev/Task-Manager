import django_filters
from django_filters.filterset import FilterSet
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.user.models import User
from task_manager.labels.models import Label
from django import forms


class TaskFilter(FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метки',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', ]
