from django import forms
from .models import Comment
from ckeditor.fields import RichTextFormField


class CommentForm(forms.ModelForm):
    """A form to add comments"""
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': RichTextFormField(config_name='default'),
        }
