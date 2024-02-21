from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

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
def index(request):
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
            "post_content": "",
            "post_media_path": "static/main/images/circle.png",
        },
        {
            "post_id": 2,
            "post_date": "01-01-3030",
            "post_author": "Someone",
            "post_replies": [3, 1, 8],
            "post_content": "",
            "post_media_path": "",
        },
        {
            "post_id": 3,
            "post_date": "01-01-3030",
            "post_author": "",
            "post_replies": [1, 4, 2],
            "post_content": "",
            "post_media_path": "",
        },
        {
            "post_id": 4,
            "post_date": "01-01-3030",
            "post_author": "Robert",
            "post_replies": [3, 1, 2],
            "post_content": "",
            "post_media_path": "",
        },
        {
            "post_id": 5,
            "post_date": "01-01-3030",
            "post_author": "",
            "post_replies": [1, 4, 8],
            "post_content": "",
            "post_media_path": "",
        },
    ]
    context = {
        "name": channel_name,
        "desc": "Channel",
        "thread_id": thread_id,
        "posts": posts,
    }
    return render(request, "main/thread.html", context)

def user_settings(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/user-settings.html", context)

def mod_panel(request, user_id):
    context = { "user_id": user_id }
    return render(request, "main/mod-panel.html", context)
