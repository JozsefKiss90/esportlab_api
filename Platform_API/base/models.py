from django.db import models


class ReactionTime(models.Model):
    rt = models.IntegerField()
    email = models.EmailField()
    acc = models.IntegerField()
    game = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"ReactionTime (ID: {self.pk}, Email: {self.email})"

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1  # Return a string representation of the object