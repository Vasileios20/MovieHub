from django.contrib import admin
from .models import Movie


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