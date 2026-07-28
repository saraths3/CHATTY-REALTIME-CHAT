from django.urls import path
from .views import chat, room

urlpatterns = [
    path('chat/',  chat, name='index'),
    path('room/<str:room_name>/', room, name='room')
]