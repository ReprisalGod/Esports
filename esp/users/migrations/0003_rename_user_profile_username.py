# Generated by Django 4.1.2 on 2024-02-28 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_avatar_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]
