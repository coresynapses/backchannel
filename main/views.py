from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

def index(request):
    return HttpResponse("Backchan Homepage")

def log_in(request):
    return HttpResponse("Backchan Login")

def create_account(request):
    return HttpResponse("Backchan Create Account")

def channel(request, channel_name):
    return HttpResponse(f"Backchan Channel: {channel_name}")

def thread(request, channel_name, thread_id):
    return HttpResponse(f"Backchan Thread {thread_id} in Channel {channel_name}")

def user_settings(request, user_id):
    return HttpResponse(f"Backchan user settings for user {user_id}")

def mod_panel(request, user_id):
    return HttpResponse(f"Backchan moderator panel for user {user_id}")
