from django.shortcuts import render
from Task_user_login.models import UserModel
from .models import Taskmodel, TaskStatus,BacklogsTaskModel
from .serializers import TaskSerializer,BackLogTaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.db.models import Q
from .metadata import ManyToManyMetaData
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.validators import ValidationError

class BackeLog_TaskView(viewsets.ModelViewSet):
     queryset = BacklogsTaskModel.objects.all()
     serializer_class = BackLogTaskSerializer
     permission_classes = [IsAuthenticated, DjangoModelPermissions]
     metadata_class=ManyToManyMetaData


     def perform_create(self, serializer):
        task_id = self.request.data.get("task")  # Assuming `task` ID is passed in the request
        if not task_id:
            raise ValidationError({"task": "This field is required."})

        try:
            task_instance = Taskmodel.objects.get(id=task_id)
        except Taskmodel.DoesNotExist:
            raise ValidationError({"task": "Task with this ID does not exist."})

        # Save the backlog instance with the related task
        serializer.save(task=task_instance)
         
     def perform_update(self, serializer):
         print("wwwwwwwwwww")
         serializer.save(task__created_by=self.request.user)
     def get_queryset(self):
        user = self.request.user
        if user.groups.name in ['HR_Admin', 'Project_Manager', 'Admin']:
         
            return BacklogsTaskModel.objects.filter(Q(task__created_by = user) | Q(task__created_by__reports_to = user))
        else:
             return BacklogsTaskModel.objects.filter(
                Q(task__assigned_to=user))    
                                                           
class TaskView(viewsets.ModelViewSet):
    queryset = Taskmodel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    metadata_class=ManyToManyMetaData

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    def perform_update(self, serializer, pk = None):
         serializer.save(created_by=self.request.user)
       
    def get_queryset(self):
        user = self.request.user
        if user.groups.name in ['HR_Admin', 'Project_Manager', 'Admin']:
         
            return Taskmodel.objects.filter(Q(created_by = user) | Q(created_by__reports_to = user))
        else:
             return Taskmodel.objects.filter(
                Q(assigned_to=user))
        
       


