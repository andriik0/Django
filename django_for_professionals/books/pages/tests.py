from django.test import SimpleTestCase
from django.test import TestCase
from django.urls import reverse, resolve

from .views import AboutPageView, HomePageView


class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url, follow=True)

    def test_homepage_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_not_contain_incorrect_html(self):
        self.assertNotContains(
                self.response, 'It should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            HomePageView.as_view().__name__,
            view.func.__name__
        )


class AboutPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url, follow=True)

    def test_aboutpage_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contain_correct_html(self):
        self.assertContains(self.response, 'About')

    def test_aboutpage_not_contain_incorrect_html(self):
        self.assertNotContains(
                self.response, 'It should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            AboutPageView.as_view().__name__,
            view.func.__name__
        )
