from django.shortcuts import render
from .models import UserModel
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from .serializers import UserModelSerializer, UserProfileSerializer
# Create your views here.

class UserModelView(viewsets.ReadOnlyModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = {
        "email": ["exact"],
    }
class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    




