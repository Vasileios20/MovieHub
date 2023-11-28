from django.test import TestCase
import json
from .models import Movie
from decimal import Decimal


class TestViews(TestCase):

    def setUp(self):
        movie = Movie.objects.create(
            movie_id=12345,
            title='test',
            overview='test overview',
            poster_path='test poster',
            release_date='2021-01-01',
            genres=json.dumps("genres"),
            cast='test actors',
            revenue=1000,
            runtime=120,
            budget=1000,
            popularity=1.5,
            homepage='test homepage',
            production_companies=json.dumps('test production company'),
            production_countries=json.dumps('test production country'),
            spoken_languages=json.dumps('test spoken languages'),
            original_language='English',
            original_title='test original title',
        )
        movie.save()

    def test_movie_model(self):
        movie = Movie.objects.get(movie_id=12345)
        self.assertEqual(movie.title, 'test')
        self.assertEqual(movie.overview, 'test overview')
        self.assertEqual(movie.poster_path, 'test poster')
        self.assertEqual(movie.release_date, '2021-01-01')
        self.assertEqual(movie.genres, json.dumps("genres"))
        self.assertEqual(movie.cast, 'test actors')
        self.assertEqual(movie.revenue, 1000)
        self.assertEqual(movie.runtime, 120)
        self.assertEqual(movie.budget, 1000)
        self.assertEqual(movie.popularity, Decimal(1.5))
        self.assertEqual(movie.homepage, 'test homepage')
        self.assertEqual(movie.production_companies,
                         json.dumps('test production company'))
        self.assertEqual(movie.production_countries,
                         json.dumps('test production country'))
        self.assertEqual(movie.spoken_languages,
                         json.dumps('test spoken languages'))
        self.assertEqual(movie.original_language, 'English')
        self.assertEqual(movie.original_title, 'test original title')
