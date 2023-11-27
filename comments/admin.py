from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'movie_id',
                    'created_on', 'updated_on', 'approved',)
    list_filter = ('approved', 'created_on', 'updated_on')
    search_fields = ('user', 'email', 'comment',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
