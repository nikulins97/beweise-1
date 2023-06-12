# beweise-1
Тестовое задание, задача 1

Сервис выполнен на основе Django, Django REST Framework. В качестве СУБД использутся PostgreSQL.

Для запуска контейнера в терминале из директории drf_api_audio выполнить команду:
docker compose up --detach

Для добавления пользователя отправить POST-запрос на url http://localhost:8000/create_user/. Пример запроса: {"username": "Sidney Crosby"}. UUID формируется и заносится в БД автоматически.

Для добавления аудиозаписи в БД отправить POST-запрос на url http://localhost:8000/add_audio/. Пример запроса: {"user_id": "1", "user_uuid": "9dcda321-a9a2-465c-a15b-d2a44d299e30", "audio": "media/sample-3s.wav"}.

Для получения аудио из БД в формате mp3 перейти по возвращённой ссылке (http://127.0.0.1:8000/get_audio/).
