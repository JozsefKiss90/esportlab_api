import json
from django.db import models


class ReactionTime(models.Model):
    rtArray = models.TextField()
    rt = models.FloatField()
    email = models.EmailField()

    def set_rtArray(self, data):
        self.rtArray = json.dumps(data)

    def get_rtArray(self):
        return json.loads(self.rtArray)
    def __str__(self):
        return f"ReactionTime (ID: {self.pk}, Email: {self.email})"

class Memory(models.Model):
    memorySpan = models.FloatField()
    email = models.EmailField()
    def __str__(self):
        return f"Memory (ID: {self.pk}, Email: {self.email})"

class Amp(models.Model):
    performance = models.CharField(max_length=255)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Amp (ID: {self.pk}, Email: {self.email})"

class HandEye(models.Model):
    performance = models.TextField()
    email = models.EmailField()

    def set_performance(self, data):
        self.performance = json.dumps(data)

    def get_performance(self):
        return json.loads(self.performance)

    def __str__(self):
        return f"HandEye (ID: {self.pk}, Email: {self.email})"

import json
from django.db import models

class Performance(models.Model):
    correct_percent = models.FloatField()
    avg_compatible_rt = models.FloatField()
    avg_incompatible_rt = models.FloatField()
    simon_effect = models.FloatField()

    def __str__(self):
        return f"Performance (ID: {self.pk})"

class SimonTask(models.Model):
    performance = models.OneToOneField(Performance, on_delete=models.CASCADE)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SimonTask (ID: {self.pk}, Email: {self.email})"

class Game(models.Model):
    game = models.CharField(max_length=255)
    email = models.EmailField()
    rank = models.CharField(max_length=255)
    best_rank = models.CharField(max_length=255)
    game_time = models.FloatField()
    age = models.IntegerField()
