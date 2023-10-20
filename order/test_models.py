from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestModels(TestCase):

    def create_ramen(self, toppings_choice=1, soup_choice=1, side_dish=1):
        return Ramen.objects.create(toppings_choice=toppings_choice, soup_choice=soup_choice, side_dish=side_dish)
    
    def test_topping_function_return_latest_choice_(self):
        topping = self.create_ramen()
        self.assertTrue(isinstance(topping, Ramen))
        self.assertEqual(topping.topping(), topping.toppings_choice)
        
        