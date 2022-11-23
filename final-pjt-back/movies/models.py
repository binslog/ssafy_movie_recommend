from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)
    

    # models.model?
class Movie(models.Model):

    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.TextField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ????

class Trend(models.Model):

    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.TextField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)

