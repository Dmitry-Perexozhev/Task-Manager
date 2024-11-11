from django.db import models
from task_manager.statuses.models import Status
from task_manager.user.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)
