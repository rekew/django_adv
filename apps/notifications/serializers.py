# Third party and Python modules
from rest_framework.serializers import ModelSerializer
# Project modules
from .models import Notification


class NotificationSerializer(ModelSerializer):
    """
    Serializer for Notification model
    """

    class Meta:
        model = Notification
        fields = "__all__"
