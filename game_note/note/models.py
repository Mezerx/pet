from django.db import models

class User(models.Model):
    player1 = models.CharField(max_length=20, blank=True)
    player2 = models.CharField(max_length=20, blank=True)
    player3 = models.CharField(max_length=20, blank=True)
    player4 = models.CharField(max_length=20, blank=True)








