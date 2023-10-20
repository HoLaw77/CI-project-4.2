from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm
# Create your tests here.

class TestViews(TestCase):

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_sushi(self):
        response = self.client.get('/sushi/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sushi/sushi.html')

    def test_get_ramen(self):
        response = self.client.get('/ramen/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ramen/ramen.html')

    def test_get_drink(self):
        response = self.client.get('/drink/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink/drink.html')
   
