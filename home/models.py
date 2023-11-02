from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()

    def __str__(self):
        return self.movie_id


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    comment = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return f'Comment {self.comment} by {self.user}'


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genres = models.TextField(max_length=200)
    cast = models.CharField(max_length=200)
    revenue = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    popularity = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True) 
    production_companies = models.CharField(max_length=200, blank=True, null=True)
    production_countries = models.CharField(max_length=200, blank=True, null=True)
    spoken_languages = models.CharField(max_length=200, blank=True, null=True)
    original_language = models.CharField(max_length=200, blank=True, null=True)
    original_title = models.CharField(max_length=200, blank=True, null=True)
    vote_average = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title