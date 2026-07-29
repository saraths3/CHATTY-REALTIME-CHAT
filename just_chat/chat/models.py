from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    passcode = models.CharField(max_length=16)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room.name} - {self.content[:10]}'
