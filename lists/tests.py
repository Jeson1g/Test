from django.urls import resolve
from django.test import TestCase
from .views import home_page
from django.http import HttpRequest


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))