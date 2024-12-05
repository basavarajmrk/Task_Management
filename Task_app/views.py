from django.shortcuts import render
from Task_user_login.models import UserModel
from .models import Taskmodel, TaskStatus
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.db.models import Q
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Taskmodel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)
        return super().perform_create(serializer)
    def perform_update(self, serializer, pk = None):
        serializer.save(created_by = self.request.user)
        return super().perform_update(serializer)
    def get_queryset(self):
        user = self.request.user
        if user.groups.name in ['HR_Admin', 'Project_Manager', 'Admin']:
         
            return Taskmodel.objects.filter(Q(created_by = user) & Q(created_by__reports_to = user))
        else:
             return Taskmodel.objects.filter(
                Q(assigned_to=user))
        
       


