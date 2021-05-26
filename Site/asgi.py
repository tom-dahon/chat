"""
ASGI config for Site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import Chat.routing
from Chat import consumers
from django.urls import re_path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Site.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"^front(end)/$", consumers.ChatConsumer.as_asgi()),
        ]),
    ),
"websocket": AuthMiddlewareStack(
        URLRouter(
            Chat.routing.websocket_urlpatterns,
        ),
    ),
})