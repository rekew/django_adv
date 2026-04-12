# Django modules
from django.db.models.signals import post_save
from django.dispatch import receiver

# Project modules
from apps.blogs.models import Comment
from .models import Notification


@receiver(post_save, sender=Comment)
def create_notification(sender, instance, created, **kwargs):
    if created:
        post_owner = instance.post.author

        if instance.author != post_owner:
            Notification.objects.create(
                recipient=post_owner,
                comment=instance
            )
