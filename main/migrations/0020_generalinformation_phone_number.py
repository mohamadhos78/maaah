# Generated by Django 3.2.15 on 2022-09-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220902_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinformation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]