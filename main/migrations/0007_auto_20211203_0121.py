# Generated by Django 3.1.7 on 2021-12-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211203_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='date',
            field=models.DateField(),
        ),
    ]