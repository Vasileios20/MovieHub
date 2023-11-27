from django.urls import path
from . import views

urlpatterns = [
    path('add_rating/', views.add_rating, name='add_rating'),
    path('ratings/', views.view_ratings, name='view_ratings'),
]