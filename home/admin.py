from django.contrib import admin
from .models import Favourites, Movie, Rating


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie_id',)
    list_filter = ('user', 'movie_id',)
    search_fields = ('user', 'movie_id',)
    actions = ['delete_favourites']

    def delete_favourites(self, request, queryset):
        queryset.delete()


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_id', 'title', 'overview', 'poster_path',
                    'release_date', 'genres', 'cast', 'revenue', 'runtime',
                    'budget', 'popularity', 'homepage', 'production_companies',
                    'production_countries', 'spoken_languages',
                    'original_language', 'original_title',)
    list_filter = ('movie_id', 'title', 'release_date',)
    search_fields = ('movie_id', 'title', 'release_date',)
    actions = ['delete_movie']

    def delete_movie(self, request, queryset):
        queryset.delete()


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie_id', 'rating',)
    list_filter = ('user', 'movie_id',)
    search_fields = ('user', 'movie_id',)
    actions = ['delete_rating']

    def delete_rating(self, request, queryset):
        queryset.delete()
