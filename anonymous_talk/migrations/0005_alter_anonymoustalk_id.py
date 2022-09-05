# Generated by Django 3.2.15 on 2022-09-05 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous_talk', '0004_alter_anonymoustalk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymoustalk',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
