from .models import Taskmodel, BacklogsTaskModel
from django.utils.timezone import now

     
def move_to_backlog():
        overdue_tasks = Taskmodel.objects.filter(due_date__lt=now()).exclude(status='Done')
        print(overdue_tasks,"ggggggggggggggggggg")
    
        for due in overdue_tasks:
            try:
                ff = BacklogsTaskModel.objects.get(task_id=due.id)
                print(ff,"ggggggggggggg")
            except BacklogsTaskModel.DoesNotExist:
                backlog = BacklogsTaskModel.objects.create(
                    task=due,   
                    original_due_date=due.due_date,
                    comments = 'add comment'
                )
                # set many to many field assigned_to to assigned_to_due
                backlog.assigned_to_due.set(due.assigned_to.all())
                backlog.save()
                # Update task status
                due.status = 'Backlog'
                due.save()