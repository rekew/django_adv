# Django modules

from django.db import models

# Project modules
from apps.users.models import User
from apps.blogs.models import Comment

class Notification(models.Model):
    """
    Model for notification in db
    """

    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="notifications"
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.email}: {self.title}"
