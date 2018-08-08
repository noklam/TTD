from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.test import TestCase

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_is_about_todo_lists(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_show_items_in_database(self):

        Item.objects.create(text='item1')
        Item.objects.create(text='item2')

        request = HttpRequest()
        responese = home_page(request)

        self.assertIn('item1', responese.content.decode())
        self.assertIn('item2', responese.content.decode())

    def test_home_page_can_save_post_requests_to_database(self):
        request = HttpRequest()    
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'

        response = home_page(request)

        item_from_db = Item.objects.all()[0]
        self.assertEqual(item_from_db.text, 'A new item')
        print(response.content)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/lists/the-only-list-in-the-world')

        # print('*'*30)
        # print(response.content.decode())
        # print(render(HttpRequest(), 'home.html').content.decode())

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items_to_the_database(self):

        first_item = Item()
        first_item.text = 'Item the first'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        first_item_from_db = Item.objects.all()[0]
        self.assertEqual(first_item_from_db.text, 'Item the first')

        second_item_from_db = Item.objects.all()[1]
        self.assertEqual(second_item_from_db.text, 'Item the second')  

class ListViewTest(TestCase):

    def test_lists_page_shows_items_in_database(self):

        Item.objects.create(text='item1')
        Item.objects.create(text='item2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertIn('item1', response.content.decode())
        self.assertContains(response,'item2')
