from django.urls import resolve
from django.test import TestCase
from .views import home_page
from .models import Item


# Create your tests here.
class HomePageTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')

        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

    # class ItemModelTest(TestCase):
#
#     def test__saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = 'The first (ever) list item'
#         first_item.save()
#
#         second_item = Item()
#         second_item.text = 'Item the second'
#         second_item.save()
#
#         items = Item.objects.all()
#
#         self.assertEqual(items.count(), 2)
#
#         first_item = items[0]
#         second_item = items[1]
#         self.assertEqual(first_item.text, 'The first (ever) list item')
#         self.assertEqual(second_item.text, 'Item the second')
