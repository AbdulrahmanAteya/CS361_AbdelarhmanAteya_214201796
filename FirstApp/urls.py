from django.conf.urls import url, include
from django.contrib import admin
from FirstApp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<game_id>[0-9])/$', views.detail, name="detail")
]

