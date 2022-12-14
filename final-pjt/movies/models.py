from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=30)

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies', default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    poster_path = models.TextField(null=True)
    overview = models.TextField()
    released_date = models.DateTimeField(auto_now=False)
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    popularity = models.IntegerField()
    runtime = models.IntegerField(null=True)
    vote_average = models.IntegerField()

    def __str__(self):
        return self.title
