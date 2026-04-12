# Third party and Python modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

# Project modules
from .models import Notification
from .serializers import NotificationSerializer


class NotificationCountView(APIView):
    """
    View to count unread notifications for the authenticated user
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        unread_notifications = Notification.objects.filter(
            recipient=request.user, is_read=False
        ).count()

        return Response({"unread_notifications": unread_notifications})


class NotificationListView(ListAPIView):
    """
    View to list notifications for the authenticated user
    """

    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-created_at")


class MarkAllReadView(APIView):
    """
    View to mark all notifications as read for the authenticated user
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        Notification.objects.filter(
            recipient=request.user, is_read=False).update(is_read=True)
        return Response({"message": "All notifications marked as read"})
