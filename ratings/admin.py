from django.contrib import admin
from .models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie_id', 'rating',)
    list_filter = ('user', 'movie_id',)
    search_fields = ('user', 'movie_id',)
    actions = ['delete_rating']

    def delete_rating(self, request, queryset):
        queryset.delete()