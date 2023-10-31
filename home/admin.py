from django.contrib import admin
from .models import Favourites, Comment


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
