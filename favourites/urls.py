from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/favourite_movie/',
         views.add_favourites, name='add_favourites'),
    path('favourites/', views.view_favourites, name='favourites'),
    path('remove_favourite/<movie_id>/',
         views.remove_favourite, name='remove_favourite'),
]
