from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomePageTest(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(200, response.status_code)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(200, response.status_code)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(1, get_user_model().objects.all().count())
        self.assertEqual(self.username,
            get_user_model().objects.all()[0].username)
        self.assertEqual(self.email, get_user_model().objects.all()[0].email)
