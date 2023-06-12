import uuid
from django.db import models


# Модель для создания пользователя
class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    user_uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.username


# Модель для добавления аудиозаписи
class Audio(models.Model):
    user_id = models.IntegerField()
    user_uuid = models.CharField(max_length=255)
    audio = models.FileField()
    audio_uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.pk


