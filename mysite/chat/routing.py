# chat/routing.py
# routing configuration for the chat app that has a route to the consumer. 
# Create a new file chat/routing.py. Your app directory should now look like:
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

# We call the as_asgi() classmethod in order to get an ASGI application 
# that will instantiate an instance of our consumer for each user-connection. 
# This is similar to Django’s as_view(), which plays the same role for per-request Django view instances.