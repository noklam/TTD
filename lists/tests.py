from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from django.shortcuts import render

class HomePageTest(TestCase):

    def test_home_page_is_about_todo_lists(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_remember_POST_requests(self):
        request = HttpRequest()    
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'
        response = home_page(request)

        self.assertIn('A new item', response.content.decode())
        expected_content = render_to_string('home.html',{'new_item_text':'A new item'})
        # print('*'*30)
        # print(response.content.decode())
        # print(render(HttpRequest(), 'home.html').content.decode())