from django.urls import resolve
from django.test import TestCase
from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
