from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm
from .forms import BookTimeForm, SushiOrder, RamenOrder, DrinkOrder


class TestDjango(TestCase):


    def test_user_name_is_required_(self):
        form = BookTimeForm({'your_name':""})
        self.assertFalse(form.is_valid())
        self.assertIn('your_name', form.errors.keys())
        self.assertEqual(form.errors['your_name'][0], 'This field is required.')


    def test_dinning_time_is_required_(self):
        form = BookTimeForm({'dinning_time':""})
        self.assertFalse(form.is_valid())
        self.assertIn('dinning_time', form.errors.keys())
        self.assertEqual(form.errors['dinning_time'][0], 'This field is required.')


    def test_arriving_date_is_required_(self):
        form = BookTimeForm({'arriving_date':""})
        self.assertFalse(form.is_valid())
        self.assertIn('arriving_date', form.errors.keys())
        self.assertEqual(form.errors['arriving_date'][0], 'This field is required.')


    def test_number_of_people_is_required_(self):
        form = BookTimeForm({'number_of_people':""})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_people', form.errors.keys())
        self.assertEqual(form.errors['number_of_people'][0], 'This field is required.')


    def test_email_is_required_(self):
        form = BookTimeForm({'email':""})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')


    def test_nigiri_option_required_(self):
        form = SushiOrder({'nigiri_sushi':""})
        self.assertFalse(form.is_valid())
        self.assertIn('nigiri_sushi', form.errors.keys())
        self.assertEqual(form.errors['nigiri_sushi'][0], 'This field is required.')


    def test_inari_option_required_(self):
        form = SushiOrder({'inari_sushi':""})
        self.assertFalse(form.is_valid())
        self.assertIn('inari_sushi', form.errors.keys())
        self.assertEqual(form.errors['inari_sushi'][0], 'This field is required.')    


    def test_maki_option_required_(self):
        form = SushiOrder({'maki_sushi':""})
        self.assertFalse(form.is_valid())
        self.assertIn('maki_sushi', form.errors.keys())
        self.assertEqual(form.errors['maki_sushi'][0], 'This field is required.')


    def test_temaki_option_required_(self):
        form = SushiOrder({'temaki_sushi':""})
        self.assertFalse(form.is_valid())
        self.assertIn('temaki_sushi', form.errors.keys())
        self.assertEqual(form.errors['temaki_sushi'][0], 'This field is required.')


    def test_soy_oil_option_required(self):
        form = SushiOrder({'soy_oil':""})
        self.assertFalse(form.is_valid())
        self.assertIn('soy_oil', form.errors.keys())
        self.assertEqual(form.errors['soy_oil'][0], 'This field is required.')


    def test_wasabi_option_required(self):
        form = SushiOrder({'wasabi':""})
        self.assertFalse(form.is_valid())
        self.assertIn('wasabi', form.errors.keys())
        self.assertEqual(form.errors['wasabi'][0], 'This field is required.')


    def test_toppings_option_required(self):
        form = RamenOrder({'toppings_choice':""})
        self.assertFalse(form.is_valid())
        self.assertIn('toppings_choice', form.errors.keys())
        self.assertEqual(form.errors['toppings_choice'][0], 'This field is required.')


    def test_soup_option_required(self):
        form = RamenOrder({'soup_choice':""})
        self.assertFalse(form.is_valid())
        self.assertIn('soup_choice', form.errors.keys())
        self.assertEqual(form.errors['soup_choice'][0], 'This field is required.')


    def test_side_dish_option_required(self):
        form = RamenOrder({'side_dish': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('side_dish', form.errors.keys())
        self.assertEqual(form.errors['side_dish'][0], 'This field is required.')


    def test_beer_option_required(self):
        form = DrinkOrder({'beer': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('beer', form.errors.keys())
        self.assertEqual(form.errors['beer'][0], 'This field is required.')


    def test_sake_option_required(self):
        form = DrinkOrder({'sake': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('sake', form.errors.keys())
        self.assertEqual(form.errors['sake'][0], 'This field is required.')


    def test_choya_option_required(self):
        form = DrinkOrder({'choya': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('choya', form.errors.keys())
        self.assertEqual(form.errors['choya'][0], 'This field is required.')


    def test_green_tea_option_required(self):
        form = DrinkOrder({'green_tea': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('green_tea', form.errors.keys())
        self.assertEqual(form.errors['green_tea'][0], 'This field is required.')


    def test_water_option_required(self):
        form = DrinkOrder({'water': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('water', form.errors.keys())
        self.assertEqual(form.errors['water'][0], 'This field is required.')
    

    def test_ramen_order_form_exclusive_for_meta(self):
        form = RamenOrder()
        self.assertEqual(form.Meta.fields, ["toppings_choice", "side_dish", "soup_choice"])


    def test_drink_order_form_exclusive_for_meta(self):
        form = DrinkOrder()
        self.assertEqual(form.Meta.fields, ["sake", "beer", "choya", "green_tea", "water"])


    def test_sushi_order_form_exclusive_for_meta(self):
        form = SushiOrder()
        self.assertEqual(form.Meta.fields, ["nigiri_sushi", "inari_sushi", "maki_sushi", "temaki_sushi", "soy_oil", "wasabi"])