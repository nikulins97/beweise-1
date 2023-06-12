from rest_framework import serializers
from .models import *

# Сериализатор для модели CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


# Сериализатор для мдели Audio
class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
