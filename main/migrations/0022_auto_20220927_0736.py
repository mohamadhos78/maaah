# Generated by Django 3.2.15 on 2022-09-27 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_voice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='voice',
            old_name='voive',
            new_name='file',
        ),
    ]
