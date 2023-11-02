from django.contrib import admin
from .models import Favourites, Comment, Movie


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie_id',)
    list_filter = ('user', 'movie_id',)
    search_fields = ('user', 'movie_id',)
    actions = ['delete_favourites']

    def delete_favourites(self, request, queryset):
        queryset.delete()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'movie_id', 'created_on', 'approved',)
    list_filter = ('approved', 'created_on',)
    search_fields = ('user', 'email', 'comment',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_id', 'title', 'overview', 'poster_path',
                    'release_date', 'genres', 'cast', 'revenue', 'runtime',
                    'budget', 'popularity', 'homepage', 'production_companies',
                    'production_countries', 'spoken_languages', 'vote_average',
                    'vote_count', 'original_language', 'original_title',)
    list_filter = ('movie_id', 'title', 'release_date',)
    search_fields = ('movie_id', 'title', 'release_date',)
    actions = ['delete_movie']

    def delete_movie(self, request, queryset):
        queryset.delete()
