from django.test import TestCase
from django.urls import resolve
from .views import index
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    # def test_bad_math(self):
    #     self.assertEqual(1+1, 3)

    def test_homepage_return_correct_html(self):
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-do list</title>', html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'tdd/index.html')

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'tdd/indesx.html')

    def test_can_save_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())