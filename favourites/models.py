from django.db import models
from django.contrib.auth.models import User
from home.models import Movie


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "favourites"

    def __str__(self):
        return f"{self.movie_id}"
