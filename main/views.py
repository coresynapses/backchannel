from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

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
    date = timezone.now()
    new_thread = Thread(channel=channel, author=name, title=title, content=content, filepath=uploaded_file, date=date)
    new_thread.save()
    context = {
        "name": channel_name,
        "desc": desc,
        "threads": threads,
    }
    return HttpResponseRedirect(f"/{channel_name}/thread/{new_thread.id}")

def thread(request, channel_name, thread_id):
    channel = Channel.objects.filter(channel_name=channel_name)
    if not channel:
        return HttpResponse("Channel not found", status=404)
    channel = channel[0]
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = Post.objects.filter(channel=channel, thread=thread)
    context = {
        "name": channel_name,
        "desc": "Channel",
        "thread": thread,
        "posts": posts,
    }
    return render(request, "main/thread.html", context)

def create_post(request, channel_name, thread_id):
    channel = Channel.objects.filter(channel_name=channel_name)
    if not channel:
        return HttpResponse("Channel not found", status=404)
    channel = channel[0]
    thread = Thread.objects.filter(channel=channel, pk=thread_id)
    if not thread:
        return HttpResponse("Thread not found", status=404)
    thread = thread[0]
    posts = Post.objects.filter(channel=channel, thread=thread)
    name = request.POST["name"]
    title = request.POST["title"]
    content = request.POST["content"]
    uploaded_file = request.POST["file"]
    date = timezone.now()
    new_thread = Thread(channel=channel, author=name, title=title, content=content, filepath=uploaded_file, date=date)
    new_thread.save()
    return HttpResponseRedirect(f"/{channel_name}/thread/{thread_id}")

def user_settings(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/user-settings.html", context)

def mod_panel(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/mod-panel.html", context)

