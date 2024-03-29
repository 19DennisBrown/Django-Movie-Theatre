# Generated by Django 5.0.3 on 2024-03-06 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_rename_movie_moviedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedmovie',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='moviedate',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bookedmovie',
            name='day',
        ),
        migrations.RemoveField(
            model_name='moviedescription',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bookedmovie',
            name='description',
        ),
        migrations.RemoveField(
            model_name='moviename',
            name='title',
        ),
        migrations.RemoveField(
            model_name='bookedmovie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='bookedmovie',
            name='isBooked',
        ),
        migrations.AddField(
            model_name='bookedmovie',
            name='movieStats',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.moviedetails'),
        ),
        migrations.DeleteModel(
            name='Moviecost',
        ),
        migrations.DeleteModel(
            name='Moviedate',
        ),
        migrations.DeleteModel(
            name='Moviedescription',
        ),
        migrations.DeleteModel(
            name='Moviename',
        ),
    ]
