# Generated by Django 3.1.2 on 2020-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=280, verbose_name='comment'),
        ),
    ]
