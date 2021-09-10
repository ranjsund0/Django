# Generated by Django 2.2 on 2021-05-10 22:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_auto_20210510_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='remarks',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='wall_message',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='wall_message_comments', to='one.Wall_message'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_by', to='one.User'),
        ),
    ]