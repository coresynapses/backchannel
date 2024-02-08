import datetime

from django.db import models
from django.utils import timezone

class Channel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Thread(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    replies = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    filepath = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    replies = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
