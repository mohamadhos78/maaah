# Generated by Django 3.2.15 on 2022-09-03 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous_talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anonymoustalk',
            options={'verbose_name': 'پیام ناشناس', 'verbose_name_plural': 'پیام های ناشناس'},
        ),
        migrations.AddField(
            model_name='anonymoustalk',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='anonymous_talk.anonymoustalk'),
        ),
    ]
