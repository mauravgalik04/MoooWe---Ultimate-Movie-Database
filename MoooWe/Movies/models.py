from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length = 50 )
    release_year = models.IntegerField()
    genre = models.CharField(max_length =20)
    cast = models.TextField()
    story = models.TextField()
    imdb_rating = models.DecimalField(max_digits = 2 , decimal_places = 1)
    your_rating = models.DecimalField(max_digits = 2 , decimal_places = 1)
    watchlist = models.BooleanField(default = False)
    poster = models.ImageField()
    landscape = models.ImageField()
    def __str__(self):
        return self.name