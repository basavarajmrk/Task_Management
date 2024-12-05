from django.contrib import admin
from .models import Taskmodel
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','status', 'priority']
    fields = (
        'title',
        'description',
        'status',
        'priority',
        'assigned_to',
        'created_by',
        'deactive_time',
    )
    search_fields = ('title',)

admin.site.register(Taskmodel, TaskAdmin)
