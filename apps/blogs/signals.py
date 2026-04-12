import json
import redis
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

r = redis.Redis(host="localhost", port=6379, db=0)


@receiver(post_save, sender=Post)
def post_published_handler(sender, instance, created, **kwargs):
    """
    Trigger when post is created or updated.
    """

    if created and instance.status == "published":
        send_event(instance)

    elif not created:
        old = Post.objects.get(pk=instance.pk)

        if old.status != "published" and instance.status == "published":
            send_event(instance)


def send_event(post):
    data = {
        "post_id": post.id,
        "title": post.title,
        "slug": post.slug,
        "author": {
            "id": post.author.id,
            "email": post.author.email,
        },
        "status": post.status.format(),
    }

    r.publish("posts", json.dumps(data))