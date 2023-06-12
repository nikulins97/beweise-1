# Generated by Django 4.1.6 on 2023-06-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio',
            field=models.FileField(default=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='audio',
            name='user_id',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='audio',
            name='user_uuid',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
