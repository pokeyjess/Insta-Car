# Generated by Django 3.1.2 on 2020-10-17 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_post', '0004_auto_20201016_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='likes',
            new_name='up_votes',
        ),
    ]