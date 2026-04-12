# Python and Third Party modules
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Django modules
from django.core.asgi import get_asgi_application

# Project modules
from settings.conf import ENV_ID, ENV_POSSIBLE_OPTIONS
from apps.notifications.routing import websocket_urlpatterns

assert ENV_ID in ENV_POSSIBLE_OPTIONS, f"Invalid env id. Possible options: {ENV_POSSIBLE_OPTIONS}"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env.{ENV_ID}')

print("🔥 ASGI ACTIVE 🔥")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns),
    )
})
