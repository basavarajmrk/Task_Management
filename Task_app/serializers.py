from .models import Taskmodel
from rest_framework import serializers
from django.db.models import Q
from Task_user_login.models import UserModel
class TaskSerializer(serializers.ModelSerializer):
    # assigned_to = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), many=True, required=False)
    # assigned_to = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), many=True, required=False)
    created_by = serializers.StringRelatedField(read_only=True)
    # def __init__(self, *args, **kwargs):
    #     request = kwargs.pop('context', {}).get("request")
    #     super().__init__(*args, **kwargs)  
    #     if request is not None:
    #         user = request.user
    #         queryset = Taskmodel.objects.filter(Q(created_by =request.user) | Q(created_by__reports_to = request.user) )
    #         print(queryset,)

    #         self.fields['assigned_to'].queryset = UserModel.objects.filter(reports_to=user)

    class Meta:
        model = Taskmodel
        fields = ['id', 'title', 'description', 'due_date','status','priority','assigned_to','created_by']
    def validate_assigned_to(self, value):
        # Get the current user (reporting manager)
        user = self.context['request'].user

        # Check if each assigned user reports to the current manager
        for user_id in value:
            assigned_user = UserModel.objects.get(id=user_id)
            if assigned_user.reports_to != user:
                raise serializers.ValidationError(f"User {assigned_user.username} does not report to you.")
        
        return value
        
