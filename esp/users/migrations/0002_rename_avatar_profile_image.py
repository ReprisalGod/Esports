# Generated by Django 4.1.2 on 2024-02-28 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='image',
        ),
    ]
