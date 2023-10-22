from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestOrderModels(TestCase):
    def setUp(self):
        test = Ramen.objects.create(
            toppings_choice= 1,
            soup_choice=1,
            side_dish=1
            )
        
    def test_model_topping(self):
        topping = Ramen.objects.last()
        print(topping)
        self.assertEqual(topping.toppings_choice, 1)

    


   