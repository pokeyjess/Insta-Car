# Generated by Django 3.1.2 on 2020-10-15 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instauser',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
