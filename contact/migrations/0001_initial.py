# Generated by Django 4.2.6 on 2023-11-15 18:25

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()])),
                ('subject', models.CharField(max_length=100)),
                ('message', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
