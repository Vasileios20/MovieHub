from .models import ContactForms
from django import forms
from ckeditor.fields import RichTextFormField


class ContactForm(forms.ModelForm):
    """
    A form to allow users to contact the site owner
    """
    class Meta:
        model = ContactForms
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': RichTextFormField(config_name='default'),
        }
