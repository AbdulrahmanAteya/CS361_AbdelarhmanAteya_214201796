# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    releaseDate = models.CharField(max_length=10)


class GameType(models.Model):
    type = models.CharField(max_length=60)
    gameDetails = models.ForeignKey(Game, on_delete=models.CASCADE)
