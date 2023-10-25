from django.contrib import admin
from .models import Favourites


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie_id',)
    list_filter = ('user', 'movie_id',)
    search_fields = ('user', 'movie_id',)
    actions = ['delete_favourites']

    def delete_favourites(self, request, queryset):
        queryset.delete()
