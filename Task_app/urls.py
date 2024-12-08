from .views import TaskView, BackeLog_TaskView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
router = DefaultRouter()

router.register(r'create_task', TaskView, basename="create_task")
router.register(r'backlog', BackeLog_TaskView, basename="backlog_task")

urlpatterns = router.urls