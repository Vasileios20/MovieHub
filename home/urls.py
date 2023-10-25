from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('search_results/<movie_id>/', views.movie_details,),
    path('<int:movie_id>/favourite_movie/', views.add_favourites, name='add_favourites'),
    path('favourites/', views.view_favourites, name='favourites'),
]
