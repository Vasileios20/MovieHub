from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "favourites"

    def __str__(self):
        return f"{self.movie_id}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, related_name='comments')
    comment = RichTextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "comments"

    def __str__(self):
        return f'{self.comment}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE,
                                 related_name='ratings')
    rating = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.movie_id}"


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
