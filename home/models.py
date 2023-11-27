from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genres = models.TextField()
    cast = models.TextField()
    revenue = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    popularity = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    production_companies = models.TextField()
    production_countries = models.TextField()
    spoken_languages = models.TextField()
    original_language = models.TextField()
    original_title = models.TextField()

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return f"{self.movie_id}"
