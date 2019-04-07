from django.urls import resolve
from django.test import TestCase
from .views import home_page
from .models import Item


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_test': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())


class ItemModelTest(TestCase):

    def test__saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        items = Item.objects.all()

        self.assertEqual(items.count(), 2)

        first_item = items[0]
        second_item = items[1]
        self.assertEqual(first_item.text, 'The first (ever) list item')
        self.assertEqual(second_item.text, 'Item the second')
