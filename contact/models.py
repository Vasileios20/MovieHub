from django.db import models
from django.core.validators import EmailValidator
from ckeditor.fields import RichTextField


class ContactForms(models.Model):
    """
    A model to store contact form submissions in the database
    """
    name = models.CharField(max_length=50)
    email = models.CharField(validators=[EmailValidator()], max_length=100)
    subject = models.CharField(max_length=100)
    message = RichTextField(null=True)

    class Meta:
        verbose_name_plural = "contact forms"

    def __str__(self):
        return f"{self.name}"
