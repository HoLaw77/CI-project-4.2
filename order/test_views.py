from django.test import TestCase
from django.urls import reverse
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.contrib.auth.models import User
# Create your tests here.

class TestURLViews(TestCase):

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
   
class TestViews(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username="Testuser", password="Password987")
        self.ramen = Ramen.objects.create(toppings_choice=1, side_dish=1, soup_choice=1)
        self.sushi = Sushi.objects.create(nigiri_sushi=1, inari_sushi=1, maki_sushi=1, temaki_sushi=1, soy_oil=1, wasabi=1)
        self.drink = Drink.objects.create(sake = 1, beer = 1, choya = 1, green_tea = 1, water =1)
        self.client.login(username="Testuser", password="Password987")
    
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
        
    def test_sushi_post_valid_form_existing_order(self):
        order = Order.objects.create(customer=self.user)
        response = self.client.post(reverse('sushi_order'), {"nigiri_sushi": 2, "inari_sushi": 2, "maki_sushi": 3, "temaki_sushi":3, "soy_oil": 1, "wasabi":2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("ramen_order"))
        order.refresh_from_db()
        self.assertEqual(order.sushi, Sushi.objects.get(nigiri_sushi= 2, inari_sushi= 2, maki_sushi= 3, temaki_sushi=3, soy_oil= 1, wasabi=2)) 
    
    def test_sushi_post_valid_form_not_existing_order(self):
        response = self.client.post(reverse('sushi_order'), {"nigiri_sushi": 1, "inari_sushi": 1, "maki_sushi": 2, "temaki_sushi":2, "soy_oil": 2, "wasabi":1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("ramen_order"))
        order = Order.objects.get(customer=self.user)
        self.assertEqual(order.sushi, Sushi.objects.get(nigiri_sushi= 1, inari_sushi= 1, maki_sushi= 2, temaki_sushi= 2, soy_oil= 2, wasabi=1)) 
    
    def test_sushi_post_valid_form_existing_order_and_ramen(self):
        order = Order.objects.create(customer=self.user)
        order.ramen = Ramen.objects.create()
        order.save()
        response = self.client.post(reverse('sushi_order'), {"nigiri_sushi": 6, "inari_sushi": 2, "maki_sushi": 3, "temaki_sushi":3, "soy_oil": 1, "wasabi":1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("drink_order"))
        order.refresh_from_db()
        self.assertEqual(order.sushi, Sushi.objects.get(nigiri_sushi = 6, inari_sushi = 2, maki_sushi = 3, temaki_sushi = 3, soy_oil = 1, wasabi = 1)) 
    
    def test_post_valid_form_existing_order_and_ramen_and_drink(self):
        order = Order.objects.create(customer=self.user)
        order.ramen = Ramen.objects.create()
        order.drink = Drink.objects.create()
        order.save()
        response = self.client.post(reverse('sushi_order'), {"nigiri_sushi": 5, "inari_sushi": 1, "maki_sushi": 2, "temaki_sushi":1, "soy_oil": 1, "wasabi":1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("order"))
        order.refresh_from_db()
        self.assertEqual(order.sushi, Sushi.objects.get(nigiri_sushi = 5, inari_sushi = 1, maki_sushi= 2, temaki_sushi = 1, soy_oil = 1, wasabi = 1)) 
    

    def test_sushi_post_invalid_form(self):
        response = self.client.post(reverse('sushi_order'), {"blah blah": "blah blah"})
        self.assertEqual(response.status_code, 200)

    def test_sushi_get_request(self):
        response = self.client.get(reverse('sushi_order'))
        self.assertEqual(response.status_code, 200)
        
    def test_drink_post_valid_form_existing_order(self):
        order = Order.objects.create(customer=self.user)
        response = self.client.post(reverse('drink_order'), {"sake": 3, "beer": 2, "choya": 2, "green_tea": 1, "water": 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("sushi_order"))
        order.refresh_from_db()
        self.assertEqual(order.drink, Drink.objects.get(sake = 3, beer = 2, choya = 2, green_tea = 1, water = 2)) 
    
    def test_post_valid_form_not_existing_order(self):
        response = self.client.post(reverse('drink_order'), {"sake": 4, "beer": 1, "choya": 4, "green_tea": 2, "water": 2})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("sushi_order"))
        order = Order.objects.get(customer=self.user)
        self.assertEqual(order.drink, Drink.objects.get(sake = 4, beer = 1, choya = 4, green_tea = 2, water = 2)) 
    
    def test_post_valid_form_existing_order_and_ramen(self):
        order = Order.objects.create(customer=self.user)
        order.ramen = Ramen.objects.create()
        order.save()
        response = self.client.post(reverse('drink_order'), {"sake": 3, "beer": 2, "choya": 1, "green_tea": 2, "water": 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("sushi_order"))
        order.refresh_from_db()
        self.assertEqual(order.drink, Drink.objects.get(sake = 3, beer = 2, choya = 1, green_tea = 2, water = 1)) 
    
    def test_post_valid_form_existing_order_and_ramen_and_sushi(self):
        order = Order.objects.create(customer=self.user)
        order.ramen = Ramen.objects.create()
        order.sushi = Sushi.objects.create()
        order.save()
        response = self.client.post(reverse('drink_order'), {"sake": 5, "beer": 5, "choya": 4, "green_tea": 2, "water": 1})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("order"))
        order.refresh_from_db()
        self.assertEqual(order.drink, Drink.objects.get(sake = 5, beer = 5, choya = 4, green_tea = 2, water = 1)) 
    

    def test_drink_post_invalid_form(self):
        response = self.client.post(reverse('drink_order'), {"blah blah": "blah blah"})
        self.assertEqual(response.status_code, 200)

    def test_drink_get_request(self):
        response = self.client.get(reverse('drink_order'))
        self.assertEqual(response.status_code, 200)
        
    
    