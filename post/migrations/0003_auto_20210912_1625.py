# Generated by Django 2.1 on 2021-09-12 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_auto_20210912_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmark_user_set',
            field=models.ManyToManyField(blank=True, related_name='bookmark_user_set', through='post.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='like_user_set', through='post.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
