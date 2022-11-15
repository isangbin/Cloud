from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)


class Actor(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    movie_id = models.IntegerField()
    # user = models.ManyToManyField(User, related_name='movies', settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    released_date = models.DateTimeField()
    popularity = models.IntegerField()
    poster_path = models.TextField()
    # genres = models.ManyToManyField(Genre, related_name='movies')
    # actors = models.ManyToManyField(Actor, related_name='movies')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
