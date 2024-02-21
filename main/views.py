from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

def index(request):
    threads = [
        { "thread_id": 1084,
          "thread_title": "Lisp General",
          "thread_author": "Myka",
          "thread_date": "01/14/82",
          "thread_content": "All things lisp:",
        },
        { "thread_id": 1234,
          "thread_title": "Combinatory Logic General",
          "thread_author": "Fred",
          "thread_date": "04/15/89",
          "thread_content": "Discuss Combinatory Logic:",
        },
    ]
    channels = [
        { 'channel_name': 'λ',
          'channel_description': 'Lisp',
          'channel_threads': threads,
          'num_threads': len(threads),
          'most_recent_thread': threads[0],
          'most_replied_thread': threads[1]
        },
        { 'channel_name': '∫',
          'channel_description': 'Math',
          'channel_threads': threads,
          'num_threads': len(threads),
          'most_recent_thread': threads[0],
          "most_replied_thread": threads[1]
        },
        { "channel_name": "ϕ",
          "channel_description": "Physics",
          "channel_threads": threads,
          "num_threads": len(threads),
          "most_recent_thread": threads[0],
          "most_replied_thread": threads[1]
        },
        { "channel_name": "ξ",
          "channel_description": "Emacs",
          "channel_threads": threads,
          "num_threads": len(threads),
          "most_recent_thread": threads[0],
          "most_replied_thread": threads[1]
        },
    ]

    context = { "channels": channels }

    return render(request, "main/index.html", context)

def log_in(request):
    return render(request, "main/log-in.html")

def create_account(request):
    return render(request, "main/create-account.html")

def channel(request, channel_name):
    context = {
        "name": channel_name,
        "desc": "Channel",
    }
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
