# Generated by Django 3.1 on 2022-08-07 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220807_2030'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='Story',
        ),
    ]