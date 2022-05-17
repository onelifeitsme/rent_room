from django.contrib import admin
from .models import Room, RoomImage


class RoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
