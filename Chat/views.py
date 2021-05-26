# chat/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login
def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def login(request):
    if request.method == 'GET':
        return render(request, 'register/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return user

        else:
            return 'Le compte n\'existe pas'

