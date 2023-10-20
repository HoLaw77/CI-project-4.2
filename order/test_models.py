from django.test import TestCase
from .models import Ramen, Sushi, Drink, Order, Confirm

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setup")
        self.your_name = Confirm.your_name("Peter Pan")

    @classmethod
    def test_your_name(self):
        super(test_your_name, cls).setUpClass()
        print(test_your_name)
        assertEqual(self.your_name, "Peter Pan")

        
        