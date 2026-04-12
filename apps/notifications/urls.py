from django.urls import path
from .views import NotificationCountView, NotificationListView, MarkAllReadView

urlpatterns = [
    path("count/", NotificationCountView.as_view(), name="notification-count"),
    path("", NotificationListView.as_view(), name="notification-list"),
    path("read/", MarkAllReadView.as_view(), name="mark-all-read"),
]
