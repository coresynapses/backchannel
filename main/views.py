from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

def index(request):
    return render(request, "main/index.html")

def log_in(request):
    return render(request, "main/log-in.html")

def create_account(request):
    return render(request, "main/create-account.html")

def channel(request, channel_name):
    context = { "name": channel_name }
    return render(request, "main/channel.html", context)

def thread(request, channel_name, thread_id):
    context = { "name": channel_name , "thread_id": thread_id}
    return render(request, "main/thread.html", context)

def user_settings(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/user-settings.html", context)

def mod_panel(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/mod-panel.html", context)
