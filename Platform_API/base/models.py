import json
from django.db import models


class ReactionTime(models.Model):
    rtArray = models.TextField()
    rt = models.IntegerField()
    email = models.EmailField()
    acc = models.IntegerField()
    game = models.CharField(max_length=100, null=True, blank=True)

    def set_rtArray(self, data):
        self.rtArray = json.dumps(data)

    def get_rtArray(self):
        return json.loads(self.rtArray)
    def __str__(self):
        return f"ReactionTime (ID: {self.pk}, Email: {self.email})"


class Game(models.Model):
    game = models.CharField(max_length=255)
    email = models.EmailField()
    rank = models.CharField(max_length=255)
    best_rank = models.CharField(max_length=255)
    game_time = models.FloatField()
    age = models.IntegerField()
