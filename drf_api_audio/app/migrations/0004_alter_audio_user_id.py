# Generated by Django 4.1.6 on 2023-06-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_audio_audio_alter_audio_user_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
