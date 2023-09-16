from django.db import models
from django.db.models import Sum
import decimal
import datetime as dt
# Create your models here.


class Ramen(models.Model):
    TOPPINGS_CHOICES = (
        (1, "Egg"),
        (2, "Sea weed"),
        (3, "Pork"),
        (4, "Garlic"),
        (5, "None")
    )

    SIDE_DISH_CHOICES = (
        (1, "Gyoza dumpling"),
        (2, "Edamame beans"),
        (3, "Yakitori skewers (chicken, beef)"),
        (4, "Tempura (Chilli squid )"),
        (5, "kimchi"),
        (6, "fried chicken"),
        (7, "None"),
    )

    SOUP_CHOICES = (
        (1, "pork bones soup"),
        (2, "Salt soup"),
        (3, "miso soup"),
        (4, "soy sauce soup"),
        (5, "None"),
    )

    price = models.DecimalField(
         max_digits=5, decimal_places=2, default=10.00)  # 22.12
    toppings_choice = models.IntegerField(
        choices=TOPPINGS_CHOICES, default=3)
    side_dish = models.IntegerField(choices=SIDE_DISH_CHOICES, default=1)
    soup_choice = models.IntegerField(
        choices=SOUP_CHOICES, default=1)

    def __str__(self) -> str:
        return "RAMEN"

    def save(self, *args, **kwargs):
        if self.toppings_choice == 1:
            self.price = decimal.Decimal(12)
        if self.toppings_choice == 2:
            self.price = decimal.Decimal(13)
        if self.toppings_choice == 3:
            self.price = decimal.Decimal(14)
        super(Ramen, self).save(*args, **kwargs)


class Sushi(models.Model):
    NIGIRI_SUSHI = (
        (1, "raw salmon x 3 "),
        (2, "raw tuna  x 3 "),
        (3, "shrimp  x 3 "),
        (4, "sea urchin  x 3 "),
        (5, "ikura  x 3 "),
        (6, "amberjack  x 3 "),
        (7, "None"),

    )

    INARI_SUSHI = (
        (1, "Inari Sushi  x 3 "),
        (2, "None"),

    )

    MAKI_SUSHI = (
        (1, "6 with 3 kinds of fish salmon, tuna, amberjack"),
        (2, "6 with cucumber, carrot and egg"),
        (3, "6 with sesame topping, cucumber, egg and crab stick inside"),
        (4, "None")
    )

    TEMAKI_SUSHI = (
        (1, " with Crab Stick, carrot and cucumber  x 3 "),
        (2, "With shrimp and cucumber  x 3 "),
        (3, "With Ikura, egg, and salad vegetables  x 3 "),
        (4, "With salmon  x 3 "),
        (5, "None")
    )

    SOY_OIL = (
        (1, "Yes"),
        (2, "No"),
    )

    WASABI = (
        (1, "Yes"),
        (2, "No"),
    )

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00)  # 22.12
    NIGIRI_SUSHI = models.IntegerField(
        choices=NIGIRI_SUSHI, default=6)
    INARI_SUSHI = models.IntegerField(
        choices=INARI_SUSHI, default=1)
    MAKI_SUSHI = models.IntegerField(
        choices=MAKI_SUSHI, default=3)
    TEMAKI_SUSHI = models.IntegerField(
        choices=TEMAKI_SUSHI, default=4)
    SOY_OIL = models.IntegerField(
        choices=SOY_OIL, default=1)
    WASABI = models.IntegerField(
        choices=WASABI, default=1)

    def __str__(self) -> str:
        return "SUSHI"

    def save(self, *args, **kwargs):
        if self.NIGIRI_SUSHI <= 3:
            self.price = decimal.Decimal(12)
        if self.NIGIRI_SUSHI >= 6:
            self.price = decimal.Decimal(15)
        if self.INARI_SUSHI <= 3:
            self.price = decimal.Decimal(12)
        if self.INARI_SUSHI >= 6:
            self.price = decimal.Decimal(15)
        if self.MAKI_SUSHI <= 3:
            self.price = decimal.Decimal(12)
        if self.MAKI_SUSHI >= 6:
            self.price = decimal.Decimal(15)
        if self.TEMAKI_SUSHI <= 3:
            self.price = decimal.Decimal(12)
        if self.TEMAKI_SUSHI >= 6:
            self.price = decimal.Decimal(15)
        super(Sushi, self).save(*args, **kwargs)


class Drink(models.Model):
    SAKE = (
        (1, "1 bottle"),
        (2, "None"),
    )
    BEER = (
        (1, "1 bottle"),
        (2, "1 can"),
        (3, "None"),
    )
    CHOYA = (
        (1, "1 bottle"),
        (2, "None"),
    )
    GREEN_TEA = (
        (1, "1 cup"),
        (2, "None"),
    )
    WATER = (
        (1, "1 cup"),
        (2, "None"),
    )

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00)  # 22.12
    SAKE = models.IntegerField(
        choices=SAKE, default=1)
    BEER = models.IntegerField(choices=BEER, default=1)
    CHOYA = models.IntegerField(choices=CHOYA, default=1)
    GREEN_TEA = models.IntegerField(choices=GREEN_TEA, default=1)
    WATER = models.IntegerField(choices=WATER, default=1)

    def __str__(self) -> str:
        return "DRINK"

    def save(self, *args, **kwargs):
        if self.SAKE == "1 bottle":
            self.price = decimal.Decimal(12)
        if self.BEER == "1 bottle":
            self.price = decimal.Decimal(5)
        if self.BEER == "1 can":
            self.price = decimal.Decimal(3)
        if self.CHOYA == "1 bottle":
            self.price = decimal.Decimal(12)
        if self.GREEN_TEA == "1 cup":
            self.price = decimal.Decimal(5)
        if self.WATER == "1 cup":
            self.price = decimal.Decimal(0)
        super(Drink, self).save(*args, **kwargs)


class Order(models.Model):
    ramen = models.ForeignKey(
        Ramen, related_name="orders", on_delete=models.CASCADE)
    sushi = models.ForeignKey(
        Sushi, related_name="orders", on_delete=models.CASCADE)
    drink = models.ForeignKey(
        Drink, related_name="orders", on_delete=models.CASCADE)
    total_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return ("ORDER")


class Confirm(models.Model):
    your_name = models.CharField(max_length=100)
    dinning_time = models.TimeField(auto_now=False, auto_now_add=False)
    arriving_date = models.DateField(auto_now=False, auto_now_add=False)
    number_of_people = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    email = models.EmailField(max_length=100)

    def save(self, *args, **kwargs):

        super(Confirm, self).save(*args, **kwargs)
