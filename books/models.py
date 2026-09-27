from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField(default=0)
    pages = models.IntegerField(default=0)
    description = models.TextField()
    summary = models.TextField()
    characters = models.CharField(max_length=500, blank=True)
    themes = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title
