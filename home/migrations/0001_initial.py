# Generated by Django 4.2.6 on 2023-11-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.CharField(max_length=200)),
                ('genres', models.TextField()),
                ('cast', models.TextField()),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('popularity', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('homepage', models.CharField(blank=True, max_length=200, null=True)),
                ('production_companies', models.TextField()),
                ('production_countries', models.TextField()),
                ('spoken_languages', models.TextField()),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
    ]
