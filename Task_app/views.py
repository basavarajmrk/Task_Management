from django.shortcuts import render
from Task_user_login.models import UserModel
from .models import Taskmodel, TaskStatus
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.db.models import Q
from .metadata import ManyToManyMetaData
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Taskmodel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    metadata_class=ManyToManyMetaData

    def perform_create(self, serializer):
        task = serializer.save(created_by=self.request.user)

        # Retrieve the reporting manager (assuming the creator is the manager)
        manager = self.request.user

        # Get all users who report to this manager
        users_reporting_to_manager = UserModel.objects.filter(reports_to=manager)

        # Assign those users to the task
        task.assigned_to.set(users_reporting_to_manager)
        return super().perform_create(serializer)
    def perform_update(self, serializer, pk = None):
         task = serializer.save(created_by=self.request.user)
         if 'assigned_to' in self.request.data:
            assigned_users = self.request.data.get('assigned_to', [])
            # Update the users assigned to the task
            task.assigned_to.set(assigned_users)
        # serializer.save(created_by = self.request.user)
         return super().perform_update(serializer)
    def get_queryset(self):
        user = self.request.user
        if user.groups.name in ['HR_Admin', 'Project_Manager', 'Admin']:
         
            return Taskmodel.objects.filter(Q(created_by = user) | Q(created_by__reports_to = user))
        else:
             return Taskmodel.objects.filter(
                Q(assigned_to=user))
        
       


