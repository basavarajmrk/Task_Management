from .models import Taskmodel
from rest_framework import serializers
from django.db.models import Q
class TaskSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField(read_only=True)
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('context', {}).get("request")
        super().__init__(*args, **kwargs)  
        if request is not None:
            queryset = Taskmodel.objects.filter(Q(created_by =request.user) | Q(created_by__reports_to = request.user) )
            print(queryset,)
            self.fields['assigned_to'].queryset = queryset

    class Meta:
        model = Taskmodel
        fields = ['id', 'title', 'description', 'due_date','status','priority','assigned_to','created_by']
