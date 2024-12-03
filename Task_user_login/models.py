from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.models import Group, Permission
from .manager import CustomUserManager
# Create your models here.
class Role(models.TextChoices):
      EMPLOYEE = 'Employee'
      MANAGER = "Manager"
      HR = "Hr"
class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    role = models.CharField(max_length=200,  choices=Role.choices, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='Custom_User_Group', null=True)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
            return self.email
    objects = CustomUserManager()

    def save(self, *args,**kwargs) -> None:
        if not self.groups:
            group = Group.objects.get(name="Candidate")
            self.groups=group
      #   if not self.is_active:
      #       self.is_active = True
        super(UserModel, self).save(*args, **kwargs)