"""
URL configuration for backchan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('log-in/', views.log_in, name="log-in"),
    path('create-account/', views.create_account, name="create-account"),
    path('<str:channel_name>/', views.channel, name="channel"),
    path('<str:channel_name>/thread/<int:thread_id>/', views.thread, name="thread"),
    path('user/<int:user_id>/settings/', views.user_settings, name="user-settings"),
    path('user/<int:user_id>/mod-panel/', views.mod_panel, name="mod-panel"),
]
