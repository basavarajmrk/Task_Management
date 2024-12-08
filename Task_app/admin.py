from django.contrib import admin
from .models import Taskmodel, BacklogsTaskModel
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','status', 'priority']
    fields = (
        'title',
        'description',
        'status',
        'priority',
        'due_date',
        'assigned_to',
        'created_by',
        'deactive_time',
    )
    search_fields = ('title',)
    # readonly_fields = ('due_date',)
class BacklogsTaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'original_due_date','moved_to_backlog_date', 'comments']
    fields = (
        'task','original_due_date','moved_to_backlog_date','assigned_to_due','comments'
    )

admin.site.register(Taskmodel, TaskAdmin)

admin.site.register(BacklogsTaskModel, BacklogsTaskModelAdmin)