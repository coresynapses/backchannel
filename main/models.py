import datetime

from django.db import models
from django.utils import timezone

class Channel(models.Model):
    channel_name = models.CharField(max_length=20)
    channel_desc = models.CharField(max_length=250, default="nodesc")
    channel_threads = models.CharField(max_length=30)

    def __str__(self):
        return self.channel_name


class Thread(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    replies = models.IntegerField(default=0)
    date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    replies = models.IntegerField(default=0)
    date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
