# Task_app/metadata.py

from rest_framework.metadata import SimpleMetadata
from Task_user_login.models import UserModel
from django.db.models import Q
from Task_user_login.serializers import UserModelSerializer

class ManyToManyMetaData(SimpleMetadata):

    def determine_metadata(self, request, view):
        metadata = super().determine_metadata(request, view)
        if hasattr(view, 'get_serializer'):
            serializer = view.get_serializer()
            if 'assigned_to' in serializer.fields:
                user=request.user
                requirements = UserModel.objects.filter(reports_to=user).values().order_by("id")
                assigned_to_options = UserModelSerializer(requirements, many=True).data
                metadata['actions']['POST']['assigned_to']['choices'] = assigned_to_options
        return metadata
