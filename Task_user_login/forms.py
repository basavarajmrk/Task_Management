from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from.models import UserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'is_staff', 'groups')
class CostomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'is_staff', 'groups')
