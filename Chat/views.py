# chat/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
import json
from .models import Message
from django.core import serializers


def index(request):
    return render(request, 'home.html')


def room(request, room_name):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'Vous devez être connecté pour accéder à cette page')
        return redirect('../../accounts/login', messages)
    else:

        messages = Message.last_10_messages()
        messagesView = []
        for message in messages:
            messagesView.append({
                'auteur' : str(message.auteur),
                'message': message.contenu
            })

        return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username': mark_safe(json.dumps(request.user.username)),
            'messages': messagesView,
        })




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def chat(request):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'Vous devez être connecté pour accéder à cette page')
        return redirect('../accounts/login', messages)
    else:
        return render(request, 'chat/index.html')

