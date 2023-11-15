from .models import ContactForms
from django import forms
from django.utils.html import strip_tags
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

    def clean_form(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')
        message = strip_tags(message)
        message = message.replace("&nbsp;", " ")
        message = str(message).strip()
        name = str(name).strip()
        email = str(email).strip()
        subject = str(subject).strip()

        if name == '':
            self.add_error('name', 'You must enter a name')
        elif email == '':
            self.add_error('email', 'You must enter an email address')
        elif subject == '':
            self.add_error('subject', 'You must enter a subject')
        elif message == '':
            self.add_error('message', 'You must enter a message')
