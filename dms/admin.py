from django.contrib import admin
from .models import ChattingRoom, Message


@admin.register(ChattingRoom)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "created_at",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "user",
        "created_at",
        "room",
    )
