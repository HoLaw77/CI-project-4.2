from django.test import TestCase
from django.urls import reverse
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.contrib.auth.models import User
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
        # self.ramen_order = Ramen.objects.create(
        #     toppings_choice= 1,
        #     soup_choice= 1,
        #     side_dish= 1,
        # )

        # self.ramen_order = reverse('ramen')
        # self.order = reverse('confirm_order')
        self.user = User.objects.create_user(username="Testuser", password="Password987")
        self.ramen = Ramen.objects.create(toppings_choice=1, side_dish=1, soup_choice=1)
        self.client.login(username="Testuser", password="Password987")
    # def testOrderGet(self):
    #     response= self.client.get(self.order)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'order.html')
    # def testRamenOrder(self):
    #     Ramen.objects.create(
    #         toppings_choice= 1,
    #         soup_choice= 1,
    #         side_dish= 1,
    #     )
        
    #     response = self.client.post(self.ramen_order, {
    #           'toppings_choice': "Egg",
    #             'soup_choice': "pork bone soup",
    #             'side_dish': "Gyoza dumpling",
    #         })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ramen/ramen.html')

    def test_post_valid_form_existing_order(self):
        order = Order.objects.create(customer=self.user)
        response = self.client.post(reverse('ramen_order'), {"toppings_choice": 2, "side_dish": 3, "soup_choice": 4})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("sushi_order"))
        order.refresh_from_db()
        self.assertEqual(order.ramen, Ramen.objects.get(toppings_choice=2, side_dish=3, soup_choice=4)) 
    
    def test_post_valid_form_not_existing_order(self):
        response = self.client.post(reverse('ramen_order'), {"toppings_choice": 3, "side_dish": 4, "soup_choice": 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("sushi_order"))
        order = Order.objects.get(customer=self.user)
        self.assertEqual(order.ramen, Ramen.objects.get(toppings_choice=3, side_dish=4, soup_choice=2)) 
    
    def test_post_valid_form_existing_order_and_sushi(self):
        order = Order.objects.create(customer=self.user)
        order.sushi = Sushi.objects.create()
        order.save()
        response = self.client.post(reverse('ramen_order'), {"toppings_choice": 1, "side_dish": 3, "soup_choice": 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("drink_order"))
        order.refresh_from_db()
        self.assertEqual(order.ramen, Ramen.objects.get(toppings_choice=1, side_dish=3, soup_choice=2)) 
    
    def test_post_valid_form_existing_order_and_sushi_and_drink(self):
        order = Order.objects.create(customer=self.user)
        order.sushi = Sushi.objects.create()
        order.drink = Drink.objects.create()
        order.save()
        response = self.client.post(reverse('ramen_order'), {"toppings_choice": 1, "side_dish": 3, "soup_choice": 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("order"))
        order.refresh_from_db()
        self.assertEqual(order.ramen, Ramen.objects.get(toppings_choice=1, side_dish=3, soup_choice=2)) 
    

    def test_post_invalid_form(self):
        response = self.client.post(reverse('ramen_order'), {"blah blah": "blah blah"})
        self.assertEqual(response.status_code, 200)

    def test_get_request(self):
        response = self.client.get(reverse('ramen_order'))
        self.assertEqual(response.status_code, 200)
        
