from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('movie_details/<movie_id>/',
         views.movie_details, name='movie_details'),
]