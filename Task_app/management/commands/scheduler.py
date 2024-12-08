import schedule
import time
from django.core.management.base import BaseCommand
from Task_app.models import Taskmodel
from Task_app.move_to_backlog import move_to_backlog
class Command(BaseCommand):
    help = 'Start the task scheduler'

    def handle(self, *args, **kwargs):
        schedule.every(5).seconds.do(move_to_backlog)

        # self.stdout.write("Scheduler started. Press CTRL+C to stop.")

        while True:
            schedule.run_pending()
            time.sleep(1)