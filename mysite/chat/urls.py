# chat/urls.py
# To call the view, we need to map it to a URL - and for this we need a URLconf.
# Create the route for the room view in chat/urls.py:
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]