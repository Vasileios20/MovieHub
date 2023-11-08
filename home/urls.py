from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('movie_details/<movie_id>/',
         views.movie_details, name='movie_details'),
    path('<int:movie_id>/favourite_movie/',
         views.add_favourites, name='add_favourites'),
    path('favourites/', views.view_favourites, name='favourites'),
    path('remove_favourite/<movie_id>/',
         views.remove_favourite, name='remove_favourite'),
    path('movie_details/<movie_id>/comments/',
         views.comment_movie, name='comment_movie'),
    path('movie_details/<movie_id>/comments/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('movie_details/<movie_id>/comments/delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('add_rating/', views.add_rating, name='add_rating'),
]
