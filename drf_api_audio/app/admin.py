from django.contrib import admin

from .models import CustomUser, Audio

admin.site.register(CustomUser)
admin.site.register(Audio)
