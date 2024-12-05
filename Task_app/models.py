from django.db import models
from Task_user_login.models import UserModel
from django.db.models import Q
# Create your models here.
class TaskStatus(models.TextChoices):
    DONE = "Done"
    INPROGRESS = 'InProgress'
    BACKLOGGED = 'Backlogged' 
class TaskPriority(models.TextChoices):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'
class Taskmodel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    due_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=50, choices=TaskStatus.choices, blank=True)
    assigned_to = models.ManyToManyField(UserModel, default=None, related_name='user_assigned_to', null=True, blank=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.RESTRICT, limit_choices_to=Q(groups__name = 'Project_Manager')| Q(
        groups__name='Admin')|Q(groups__name = 'HR_Admin'))
    priority = models.CharField(max_length=50, choices=TaskPriority.choices, blank=True)       
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deactive_time = models.DateTimeField(null=True,blank=True)

    