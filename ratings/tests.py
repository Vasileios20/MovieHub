from django.test import TestCase
from django.urls import reverse
from .models import Rating
from django.contrib.auth.models import User
from home.models import Movie
from decimal import Decimal
from .views import rating_average, ratings_list
import json


class TestRatingModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')

        self.movie = Movie.objects.create(
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
        self.movie.save()
        self.movie_1 = Movie.objects.create(
            id=2,
            movie_id=123456,
            title='test1',
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
        self.movie_1.save()
        self.rating = Rating.objects.create(
            user=self.user,
            movie_id=self.movie,
            rating=5,
        )
        self.rating.save()
        self.rating = Rating.objects.create(
            user=self.user,
            movie_id=self.movie_1,
            rating=1,
        )
        self.rating.save()
        self.rating_1 = Rating.objects.create(
            user=self.user,
            movie_id=self.movie,
            rating=4,
        )
        self.rating_1.save()
        self.rating_1 = Rating.objects.create(
            user=self.user,
            movie_id=self.movie_1,
            rating=4,
        )
        self.rating_1.save()

        self.width = str(rating_average(self.movie.movie_id) * 100 / 5) + '%'
        self.width_1 = str(rating_average(
            self.movie_1.movie_id) * 100 / 5) + '%'

        self.movie_obj = Movie.objects.get(movie_id=self.movie.movie_id)
        self.movie_obj_1 = Movie.objects.get(movie_id=self.movie_1.movie_id)

    def test_view_ratings_page(self):
        response = self.client.get(reverse('view_ratings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ratings.html')

    def test_add_rating(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_rating'), args=[1],
                                    data={'rating': 5, 'movie_id': 1})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'success': True}
        )

    def test_rating_average(self):
        self.assertEqual(rating_average(12345), 4.5)

    def test_ratings_list(self):
        self.assertEqual(ratings_list(), [[
            {
                'title': 'test',
                'poster_path': 'test poster',
                'overview': 'test overview',
                'release_date': '2021-01-01',
                'revenue': 1000,
                'budget': 1000,
                'runtime': 120,
                'popularity': Decimal('1.5'),
                'homepage': 'test homepage',
                'production_companies': 'test production company',
                'production_countries': 'test production country',
                'spoken_languages': 'test spoken languages',
                'original_language': 'English',
                'original_title': 'test original title',
                'cast': 'test actors', 'genres': 'genres',
                'movie_id': 1,
                'movie_obj': self.movie_obj.movie_id,
                'width': self.width
            },
            {
                'title': 'test1',
                'poster_path': 'test poster',
                'overview': 'test overview',
                'release_date': '2021-01-01',
                'revenue': 1000,
                'budget': 1000,
                'runtime': 120,
                'popularity': Decimal('1.5'),
                'homepage': 'test homepage',
                'production_companies': 'test production company',
                'production_countries': 'test production country',
                'spoken_languages': 'test spoken languages',
                'original_language': 'English',
                'original_title': 'test original title',
                'cast': 'test actors',
                'genres': 'genres',
                'movie_id': 2,
                'movie_obj': self.movie_obj_1.movie_id,
                'width': self.width_1
            }
        ]])
