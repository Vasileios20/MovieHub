from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie
import json


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.movie = Movie.objects.create(
            movie_id=1896,
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

    def test_get_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_search_results(self):
        response = self.client.get(reverse('search'), {'query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

    def test_search_results_blank_query(self):
        response = self.client.get(reverse('search'), {'query': ''})
        self.assertEqual(response.status_code, 302)

    def test_get_movie_details(self):
        response = self.client.get(reverse('movie_details',
                                           args=[self.movie.movie_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_details.html')

    def test_get_movie_details_not_in_db(self):
        response = self.client.get(reverse('movie_details',
                                           args=[123]))
        self.assertEqual(response.status_code, 302)
