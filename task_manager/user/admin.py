from django.contrib import admin
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.user.models import User

admin.site.register(User)
admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Task)
