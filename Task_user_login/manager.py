from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group
# from django.utils.translation import ugettext_lazy as _

class CustomUserManager (BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))
        Candidate, _ = Group.objects.get_or_create(name='Candidate')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault( 'groups' , Candidate)
        user.set_password(password)
        user.save()
        return user
    def sueper_user(self, email, password=None, **extra_fileds):
        Admin, _= Group.objects.get_or_create(name='Admin')
        extra_fileds.setdefault('is_staff', True) 
        extra_fileds.setdefault('is_active', True) 
        extra_fileds.setdefault('is_superuser', True)
        extra_fileds.setdefault('groups', Admin)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fileds) 
        