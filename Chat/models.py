from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    auteur = models.ForeignKey(User, related_name="auteur_message", on_delete=models.CASCADE) # Auteur du message
    contenu = models.TextField() # Contenu du message
    timestamp = models.DateTimeField(auto_now_add=True) # Date du message

    def __str__(self):
        return self.auteur.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10] # Retourne les 10 derniers messages en fonction de la date