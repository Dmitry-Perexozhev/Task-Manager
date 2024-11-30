import django_filters

from django_filters.filterset import FilterSet

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.user.models import User


class TaskFilter(FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель',
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', ]
