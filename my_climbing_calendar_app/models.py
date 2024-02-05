from django.db import models

class Day(models.Model):
    date = models.DateField()
    comment = models.TextField(blank=True)

class Note(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()
