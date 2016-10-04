from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.IntegerField()
    position = models.CharField(max_length=20)
    goals = models.IntegerField()
    assists = models.IntegerField()
    saves = models.IntegerField()
    team = models.CharField(max_length=25)
