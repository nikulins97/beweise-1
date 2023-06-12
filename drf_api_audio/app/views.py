from pydub import AudioSegment
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import CustomUser, Audio
from app.serializers import UserSerializer, AudioSerializer


# Класс представления для создания пользователя (обработка исключений предусмотрена базовым классом)
class UserAPICreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Класс представления для сохранения аудиозаписи в БД и её скачивания
class AudioAPICreate(APIView):

    def post(self, request):
        data = request.data

        # Преобразование wav в mp3
        input_wav = data["audio"]
        output_mp3 = "../output_mp3.mp3"
        sound = AudioSegment.from_mp3(input_wav)
        sound.export(output_mp3, format="wav")

        # Добавление данных в БД
        try:
            Audio.objects.create(
                user_id=data["user_id"],
                user_uuid=data["user_uuid"],
                audio=output_mp3,
            )
        except:
            raise TypeError("Неверный тип данных")

        return Response("http://127.0.0.1:8000/get_audio/")


# Класс представления для получения аудиозаписи из БД
class GetAudio(APIView):

    def get(self, request):
        try:
            res = Audio.objects.latest('pk')
            return Response(AudioSerializer(res).data["audio"])
        except:
            raise NotImplementedError("Не удалось подключиться к БД")
