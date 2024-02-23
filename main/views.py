from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import models

threads = [
    { "thread_id": 1084,
      "thread_title": "/lg/ - Lisp General",
      "thread_author": "Myka",
      "thread_date": "01/14/82",
      "thread_content": """Lisp is a family of programming languages with a long history and a\n
  distinctive parenthesized prefix notation. There are many dialects\n
  of Lisp, including Common Lisp, Scheme, Clojure and Elisp.\n
\n
  Emacs is an extensible, customizable, self-documenting free/libre\n
  text editor and computing environment, with a Lisp interpreter at\n
  its core.\n
\n
  >Emacs Resources\n
  https://gnu.org/s/emacs (Site)\n
  https://github.com/emacs-tw/awesome-emacs (Awesome Emacs)\n
\n
  >Learning Emacs\n
  C-h t (Interactive Tutorial)\n
  https://emacs.amodernist.com (Configuration Generator)\n
  https://systemcrafters.net/emacs-from-scratch (Emacs from Scratch)\n
  http://xahlee.info/emacs (Xah Emacs Tutorial)\n
\n
  >Emacs Distros\n
  https://spacemacs.org (Spacemacs)\n
  https://doomemacs.org (Doom Emacs)\n
  https://ergoemacs.github.io (Ergoemacs)\n
  https://portacle.github.io (Portacle)\n
\n
  >Elisp\n
  Docs: C-h f [function] C-h v [variable] C-h k [keybinding] C-h m [mode] M-x ielm [REPL]\n
  https://gnu.org/s/emacs/manual/eintr.html (Introduction to Elisp)\n
  https://gnu.org/s/emacs/manual/elisp.html (Elisp Manual)\n
\n
  >Common Lisp\n
  https://stevelosh.com/blog/2018/08/a-road-to-common-lisp (A Road to Common Lisp)\n
  https://gigamonkeys.com/book (PCL)\n
  https://cs.cmu.edu/~dst/LispBook (CL: A Gentle Introduction)\n
  https://lem-project.github.io (CL editor/IDE)\n
\n
  >Scheme\n
  https://scheme.com/tspl4 (The Scheme Programming Language)\n
  https://eecs.berkeley.edu/~bh/ss-toc2.html (Simply Scheme)\n
  https://archive.org/details/Schemer (Books)\n
\n
  >Clojure\n
  https://clojure.org (Site)\n
  https://clojure-doc.org (Docs)\n
  https://mooc.fi/courses/2014/clojure (Functional programming with Clojure)\n
\n
  >Guix\n
  https://guix.gnu.org/manual/devel (Guix Manual)\n
  https://systemcrafters.net/craft-your-system-with-guix (Introduction to Guix)\n
\n
  >SICP/HtDP\n
  https://web.mit.edu/6.001/6.037/sicp.pdf\n
  https://htdp.org\n
\n
  >More Lisp Resources\n
  https://paste.textboard.org/52b08691""",
    },
    { "thread_id": 1234,
      "thread_title": "/clg/ - Combinatory Logic General",
      "thread_author": "Fred",
      "thread_date": "04/15/89",
      "thread_content": "Discuss Combinatory Logic:",
    },
    { "thread_id": 1084,
      "thread_title": "/lg/ - Lisp General",
      "thread_author": "Myka",
      "thread_date": "01/14/82",
      "thread_content": "All things lisp:",
    },
    { "thread_id": 1234,
      "thread_title": "/clg/ - Combinatory Logic General",
      "thread_author": "Fred",
      "thread_date": "04/15/89",
      "thread_content": "Discuss Combinatory Logic:",
    },
    { "thread_id": 1084,
      "thread_title": "/lg/ - Lisp General",
      "thread_author": "Myka",
      "thread_date": "01/14/82",
      "thread_content": "All things lisp:",
     },
    { "thread_id": 1234,
      "thread_title": "/clg/ - Combinatory Logic General",
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
