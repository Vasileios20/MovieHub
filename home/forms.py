from django import forms
from .models import Comment
from ckeditor.fields import RichTextFormField
from django.utils.html import strip_tags


class CommentForm(forms.ModelForm):
    """A form to add comments"""
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': RichTextFormField(config_name='default'),
        }

    def clean_comment(self):
        """Remove html tags from comment"""
        comment = self.cleaned_data.get('comment')
        comment = strip_tags(comment)
        comment = comment.replace("&nbsp;", " ")
        comment = str(comment).strip()

        if comment == '':
            raise forms.ValidationError("You can't submit an empty comment")

        return comment
