# chat/views.py
from django.shortcuts import render

# view function for the room view.
def index(request):
    return render(request, 'template/chat/index.html')

def room(request, room_name):
    return render(request, 'template/chat/room.html', {
        'room_name': room_name
    })