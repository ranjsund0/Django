# Generated by Django 2.2 on 2021-05-10 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wall_message',
            name='message_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to='one.User'),
        ),
    ]
