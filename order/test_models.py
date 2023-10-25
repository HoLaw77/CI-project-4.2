from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestOrderModels(TestCase):

    def setUp(self):
        Ramen.objects.create(
            toppings_choice= 1,
            soup_choice=1,
            side_dish=1
            )
        
    def test_model_topping(self):
        topping = Ramen()
        self.assertEqual(topping.topping, 'Egg')
   
    def test_model_side_dish(self):
        side_dish = Ramen()
        self.assertEqual(side_dish.side, 'Gyoza dumpling')

    def test_model_soup_choice(self):
        soup = Ramen()
        self.assertEqual(soup.soup, 'pork bones soup')

    


   