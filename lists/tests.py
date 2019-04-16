from django.urls import resolve
from django.test import TestCase
from .views import home_page
from .models import Item, List


# Create your tests here.
class NewListTest(TestCase):

    def test_redirects_after_POST(self):

        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')


class NewTempTest(TestCase):

    def test_passes_correct_list_to_template(self):

        other_list = List.objects.create()
        correct_list = List.objects.create()

        rsp = self.client.get(f'/lists/{correct_list.id}/')

        self.assertEqual(rsp.context["list"], correct_list)