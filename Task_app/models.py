from django.db import models
from Task_user_login.models import UserModel
from django.db.models import Q
from django.utils.timezone import now
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
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=TaskStatus.choices, blank=True)
    assigned_to = models.ManyToManyField(UserModel, default=None, related_name='user_assigned_to', null=True, blank=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.RESTRICT, limit_choices_to=Q(groups__name = 'Project_Manager')| Q(
        groups__name='Admin')|Q(groups__name = 'HR_Admin'))
    priority = models.CharField(max_length=50, choices=TaskPriority.choices, blank=True)       
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deactive_time = models.DateTimeField(null=True,blank=True)

    

class BacklogsTaskModel(models.Model):
    task = models.ForeignKey(Taskmodel, on_delete=models.CASCADE, related_name="back_log_task", null=True, blank=True)
    original_due_date = models.DateTimeField(null=True, blank=True)
    moved_to_backlog_date = models.DateTimeField(default=now)
    assigned_to_due = models.ManyToManyField(UserModel, default=None, related_name='user_Back_assigned_to', blank=True)
    comments = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return  f"Backlog for Task: {self.task.title}"
    

    