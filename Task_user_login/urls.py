from rest_framework.routers import DefaultRouter
from .views import UserModelView, UserProfileView

router = DefaultRouter()
router.register(r'user', UserModelView, basename='user')
router.register(r'profile', UserProfileView, basename='profile')
urlpatterns = router.urls