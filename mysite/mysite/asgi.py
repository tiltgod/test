"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# mysite/asgi.py
# creating a root routing configuration for Channels. 
# A Channels routing configuration is an ASGI application that is similar to a Django URLconf, 
# in that it tells Channels what code to run when an HTTP request is received by the Channels server
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# point the root routing configuration at the chat.routing module. 
# In mysite/asgi.py, import AuthMiddlewareStack, URLRouter, and chat.routing; 
# and insert a 'websocket' key in the ProtocolTypeRouter list in the following format:
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})