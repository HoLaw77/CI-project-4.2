from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestModels(TestCase):

    def test_topping_function_return_latest_choice_(self):
        topping = Ramen.toppings_choice.create(1)
        self.assertEqual(topping(topping), 1)
        
        