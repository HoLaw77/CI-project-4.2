from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestModels(TestCase):

    def setUp(self):
        Ramen.objects.create(
            toppings_choice= 1,
            soup_choice=1,
            side_dish=1
            )
        Sushi.objects.create(
            nigiri_sushi = 1,
            inari_sushi = 1,
            maki_sushi = 1,
            temaki_sushi = 1,
            soy_oil = 1,
            wasabi = 1,
        )

        Drink.objects.create(
            sake = 1,
            beer = 1,
            choya = 1,
            green_tea = 1,
            water = 1,
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

    def test_model_nigiri(self):
        nigiri = Sushi()
        self.assertEqual(nigiri.nigiri, "raw salmon x 3 ")

    def test_model_inari(self):
        inari = Sushi()
        self.assertEqual(inari.inari, "Inari Sushi  x 3 ")

    def test_model_maki(self):
        maki = Sushi()
        self.assertEqual(maki.maki, "salmon, tuna, amberjack x 6")

    def test_model_temaki(self):
        temaki = Sushi()
        self.assertEqual(temaki.temaki, "Crab, cucumber x 3 ")

    def test_model_soy_oil(self):
        soy_oil = Sushi()
        self.assertEqual(soy_oil.soy, "Yes")

    def test_model_wasabi(self):
        wasabi = Sushi()
        self.assertEqual(wasabi.wasabi_choice, "Yes")

    def test_model_sake(self):
        sake = Drink()
        self.assertEqual(sake.sake_choice, "1 bottle Dassai Sake")

    def test_model_beer(self):
        beer = Drink()
        self.assertEqual(beer.beer_choice, "1 bottle Asahi Super Dry")

    def test_model_choya(self):
        choya = Drink()
        self.assertEqual(choya.choya_choice, "1 bottle original favor")

    def test_model_green_tea(self):
        green = Drink()
        self.assertEqual(green.green_tea_choice, "1 cup")

    def test_model_water(self):
        water = Drink()
        self.assertEqual(water.water_choice, "1 cup")

    def test_model_order_price(self):
        price = Order()
        self.assertEqual(price.total_price, 0.0)