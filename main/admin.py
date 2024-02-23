from django.contrib import admin

from .models import Channel, Thread, Post

admin.site.register(Channel)
admin.site.register(Thread)
admin.site.register(Post)
