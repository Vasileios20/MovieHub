from django.db import models
from django.contrib.auth.models import User


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

    def __str__(self):
        return self.movie_id
