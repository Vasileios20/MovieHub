from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Movie
from .models import Favourites
import json


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
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
        self.favourites = Favourites.objects.create(
            movie_id=self.movie,
            user=self.user,
        )
        self.favourites.save()

    def test_get_favourites_page(self):
        response = self.client.get(reverse('favourites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourites.html')

    def test_add_favourites(self):
        response = self.client.post(reverse('add_favourites',
                                            args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_remove_favourites(self):
        response = self.client.post(reverse('remove_favourite',
                                            args=[1]))
        self.assertEqual(response.status_code, 302)
