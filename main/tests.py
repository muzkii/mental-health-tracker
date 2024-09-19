from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="LUMAYAN SENANG",
          time = now,
          feelings = "senang sih, cuman tadi baju aku basah kena hujan :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)
    
    def setUp(self):
        # create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_main_template_uses_correct_page_title(self):
        # log in the test user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('main:show_main'))
        html_response = response.content.decode('utf-8')
        self.assertIn('PBD Mental Health Tracker', html_response)