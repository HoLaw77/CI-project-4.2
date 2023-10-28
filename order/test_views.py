from django.test import TestCase
from django.urls import reverse
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
   
class TestRamenViews(TestCase):

    def setUp(self):
        self.ramen_order = Ramen.objects.create(
            toppings_choice= 1,
            soup_choice= 1,
            side_dish= 1,
        )

        self.ramen_order = reverse('ramen')
        self.order = reverse('confirm_order')

    # def testOrderGet(self):
    #     response= self.client.get(self.order)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'order.html')
    def testRamenOrder(self):
        Ramen.objects.create(
            toppings_choice= 1,
            soup_choice= 1,
            side_dish= 1,
        )
        
        response = self.client.post(self.ramen_order, {
              'toppings_choice': "Egg",
                'soup_choice': "pork bone soup",
                'side_dish': "Gyoza dumpling",
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ramen/ramen.html')

