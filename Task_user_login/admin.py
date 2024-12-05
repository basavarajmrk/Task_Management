from django.contrib import admin
from .forms import CostomUserChangeForm, CustomUserCreationForm
from .models import UserModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CostomUserChangeForm
    model = UserModel
    list_display=(
        'username',
        'email',
        'groups',
        'is_staff',
        'is_active',
        'is_superuser',

    )
    list_filter = (
        'email',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (
            None, 
            {
                "fields": (
                    'username',
                    'password',
                    'email',
                    'groups',
                    'reports_to',


                )
            },
        ),
        (
            "Rights",
            {
                'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                )
            }
        ),
        (
            "Permissions", {
                'fields':
                ('user_permissions',)
            }
        ),

    )
    add_fieldsets = (
        (None,
        {
            "classes": ("wide",),
            'fields':
            (
             'username',
             'email',
             'password1',
             'password2',
             'groups',
             'reports_to',
             'is_active',
             'is_staff',
             'is_superuser',

            ),
        },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(UserModel, CustomUserAdmin)



