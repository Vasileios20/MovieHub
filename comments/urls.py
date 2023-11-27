from django.urls import path
from . import views


urlpatterns = [
    path('movie_details/<movie_id>/comments/',
         views.comment_movie, name='comment_movie'),
    path('movie_details/<movie_id>/comments/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('movie_details/<movie_id>/comments/delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
]
