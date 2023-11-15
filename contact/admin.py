from django.contrib import admin
from .models import ContactForms


@admin.register(ContactForms)
class ContactAdmin(admin.ModelAdmin):
    """
    A model admin to allow admin to view contact form submissions
    """

    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )
    list_filter = ('name', 'email', 'subject',)
    search_fields = ('name', 'email', 'subject',)
