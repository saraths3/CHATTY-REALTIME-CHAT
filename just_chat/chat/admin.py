from django.contrib import admin

# Register your models here.
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_filter = ('created_at','user')
    readonly_fields = ('created_at',)
    search_fields = ('name','user__username')
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'user')
    readonly_fields = ('created_at',)
    search_fields = ('user__username', 'room__name')
    ordering = ('-created_at',)