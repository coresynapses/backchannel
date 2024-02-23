from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Channel, Thread, Post

def index(request):
    channels = Channel.objects.all()
    context = { "channels": channels }

    return render(request, "main/index.html", context)

def log_in(request):
    return render(request, "main/log-in.html")

def create_account(request):
    return render(request, "main/create-account.html")

def channel(request, channel_name):
    channel = Channel.objects.filter(channel_name=channel_name)
    if not channel:
        return HttpResponse("Channel not found", status=404)
    channel = channel[0]
    threads = Thread.objects.filter(channel=channel)
    desc = channel.channel_desc
    context = {
        "name": channel_name,
        "desc": desc,
        "threads": threads,
    }
    return render(request, "main/channel.html", context)

def create_thread(request, channel_name):
    channel = Channel.objects.filter(channel_name=channel_name)[0]
    threads = Thread.objects.filter(channel=channel)
    desc = channel.channel_desc
    name = request.POST["name"]
    title = request.POST["title"]
    content = request.POST["content"]
    uploaded_file = request.POST["file"]
    new_thread = Thread(channel=channel, author=name, title=title, content=content, filepath=uploaded_file)
    new_thread.save()
    context = {
        "name": channel_name,
        "desc": desc,
        "threads": threads,
    }
    return render(request, "main/channel.html", context)

def thread(request, channel_name, thread_id):
    posts = [
        {
            "post_id": 1,
            "post_date": "01-01-3030",
            "post_author": "Anyone",
            "post_replies": [13, 14, 82],
            "post_content": "This is post 1",
            "post_media_path": "/static/main/images/circle.png",
        },
        {
            "post_id": 2,
            "post_date": "01-01-3030",
            "post_author": "Someone",
            "post_replies": [3, 1, 8],
            "post_content": "This is post 2",
            "post_media_path": "",
        },
        {
            "post_id": 3,
            "post_date": "01-01-3030",
            "post_author": "",
            "post_replies": [1, 4, 2],
            "post_content": "This is post 3",
            "post_media_path": "/static/main/images/circle.png",
        },
        {
            "post_id": 4,
            "post_date": "01-01-3030",
            "post_author": "Robert",
            "post_replies": [3, 1, 2],
            "post_content": "This is post 4",
            "post_media_path": "",
        },
        {
            "post_id": 5,
            "post_date": "01-01-3030",
            "post_author": "",
            "post_replies": [1, 4, 8],
            "post_content": "This is post 5",
            "post_media_path": "",
        },
    ]
    context = {
        "name": channel_name,
        "desc": "Channel",
        "thread": threads[0],
        "posts": posts,
    }
    return render(request, "main/thread.html", context)

def user_settings(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/user-settings.html", context)

def mod_panel(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/mod-panel.html", context)
