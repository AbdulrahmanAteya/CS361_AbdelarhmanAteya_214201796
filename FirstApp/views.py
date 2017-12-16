# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Gamers:', object)

def detail(request, game_id):
    return HttpResponse("<h2>Details for Game ID: " + str(game_id) + "</h2>")