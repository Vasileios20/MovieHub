# Generated by Django 4.2.6 on 2023-11-02 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_movie_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie'),
        ),
    ]