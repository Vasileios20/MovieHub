from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from home.models import Movie


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='comments')
    comment = RichTextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "comments"

    def __str__(self):
        return f'{self.comment}'
