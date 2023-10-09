from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
import decimal
from datetime import datetime
# Create your models here.


class Ramen(models.Model):
    TOPPINGS_CHOICES = (
        (1, "Egg"),
        (2, "Sea weed"),
        (3, "Pork"),
        (4, "Corn"),
        (5, "None"),
    )

    TOPPING_CHOICES_PRICE = (
        (1, 3),
        (2, 3),
        (3, 3),
        (4, 3),
        (5, 0),

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

    SIDE_DISH_PRICE = (
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 0),
    )

    SOUP_CHOICES = (
        (1, "pork bones soup"),
        (2, "Salt soup"),
        (3, "miso soup"),
        (4, "soy sauce soup"),
        (5, "None"),
    )

    SOUP_PRICE = (
        (1, 3),
        (2, 2),
        (3, 3),
        (4, 2),
        (5, 0),
    )

    price = models.DecimalField(
         max_digits=5, decimal_places=2, default=10.00, null=True, blank=True)  # 22.12
    toppings_choice = models.IntegerField(
        choices=TOPPINGS_CHOICES, default=3)
    side_dish = models.IntegerField(choices=SIDE_DISH_CHOICES, default=1)
    soup_choice = models.IntegerField(
        choices=SOUP_CHOICES, default=1)
    # customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def topping(self):
        return self.TOPPINGS_CHOICES[self.toppings_choice-1][1]
    
    @property
    def side(self):
        return self.SIDE_DISH_CHOICES[self.side_dish-1][1]
    
    @property
    def soup(self):
        return self.SOUP_CHOICES[self.soup_choice-1][1]
    
    def save(self, *args, **kwargs):
        price = self.TOPPING_CHOICES_PRICE[self.topping_choice-1][1] + self.SIDE_DISH_PRICE[self.side_dish-1][1] + self.SOUP_PRICE[self.soup_choice-1][1] 
        self.price = decimal.Decimal(price)

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
    
    NIGIRI_SUSHI_PRICE = (
        (1, 10),
        (2, 10),
        (3, 10),
        (4, 10),
        (5, 10),
        (6, 10),
        (7, 0),
    )

    INARI_SUSHI = (
        (1, "Inari Sushi  x 3 "),
        (2, "None"),

    )
    
    INARI_SUSHI_PRICE = (
        (1, 3),
        (2, 0),
        
    )

    MAKI_SUSHI = (
        (1, "6 with 3 kinds of fish salmon, tuna, amberjack"),
        (2, "6 with cucumber, carrot and egg"),
        (3, "6 with sesame topping, cucumber, egg and crab stick inside"),
        (4, "None")
    )
    
    MAKI_SUSHI_PRICE = (
        (1, 10),
        (2, 10),
        (3, 10),
        (4, 0),
    )

    TEMAKI_SUSHI = (
        (1, " with Crab Stick, carrot and cucumber  x 3 "),
        (2, "With shrimp and cucumber  x 3 "),
        (3, "With Ikura, egg, and salad vegetables  x 3 "),
        (4, "With salmon  x 3 "),
        (5, "None")
    )
    
    TEMAKI_SUSHI_PRICE = (
        (1, 10),
        (2, 10),
        (3, 10),
        (4, 10),
        (5, 0),
    )

    SOY_OIL = (
        (1, "Yes"),
        (2, "No"),
    )
    
    SOY_OIL_PRICE = (
        (1, 1),
        (2, 0),
    )

    WASABI = (
        (1, "Yes"),
        (2, "No"),
    )
    
    WASABI_PRICE = (
        (1, 1),
        (2, 0),
    )

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00, null=True, blank=True)  # 22.12
    nigiri_sushi = models.IntegerField(
        choices=NIGIRI_SUSHI, default=6)
    inari_sushi = models.IntegerField(
        choices=INARI_SUSHI, default=1)
    maki_sushi = models.IntegerField(
        choices=MAKI_SUSHI, default=3)
    temaki_sushi = models.IntegerField(
        choices=TEMAKI_SUSHI, default=4)
    soy_oil = models.IntegerField(
        choices=SOY_OIL, default=1)
    wasabi = models.IntegerField(
        choices=WASABI, default=1)
    # customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    
    @property
    def nigiri(self):
        return self.NIGIRI_SUSHI[self.nigiri_sushi-1][1]
    
    @property
    def inari(self):
        return self.INARI_SUSHI[self.inari_sushi-1][1]
    
    @property
    def maki(self):
        return self.MAKI_SUSHI[self.maki_sushi-1][1]
    
    @property
    def temaki(self):
        return self.TEMAKI_SUSHI[self.temaki_sushi-1][1]
    
    @property
    def soy(self):
        return self.SOY_OIL[self.soy_oil-1][1]
    
    @property
    def wasabi_choice(self):
        return self.WASABI[self.wasabi-1][1]
    # def __str__(self) -> str:
    #     return "SUSHI"

    def save(self, *args, **kwargs):
        price = self.NIGIRI_SUSHI_PRICE[self.nigiri_sushi-1][1] + self.INARI_SUSHI_PRICE[self.inari_sushi-1][1] + self.MAKI_SUSHI_PRICE[self.maki_sushi-1][1] + self.TEMAKI_SUSHI_PRICE[self.temaki_sushi-1][1] + self.SOY_OIL_PRICE[self.soy_oil-1][1] + self.WASABI_PRICE[self.wasabi-1][1]
        self.price = decimal.Decimal(price)
       
                    
        super(Sushi, self).save(*args, **kwargs)


class Drink(models.Model):
    SAKE = (
        (1, "1 bottle Dassai Sake"),
        (2, "1 bottle Kubota Sake"),
        (3, "1 bottle Yamamoto Sake"),
        (4, "1 bottle Juyondai Sake"),
        (5, "None"),
    )

    SAKE_PRICE = (
        (1, 15),
        (2, 12),
        (3, 12),
        (4, 13),
        (5, 0),
    )
    BEER = (
        (1, "1 bottle Asahi Super Dry"),
        (2, "1 bottle Saporro Premium"),
        (3, "1 bottle Echigo Koshihikari"),
        (4, "1 bottle Orion Premium Draft Beer"),
        (5, "None"),
    )

    BEER_PRICE = (
        (1, 7),
        (2, 7),
        (3, 7),
        (4, 7),
        (5, 0),
        
    )
    CHOYA = (
        (1, "1 bottle original favor"),
        (2, "1 bottle hoeny favor"),
        (3, "1 bottle peach favor"),
        (4, "None"),
    )

    CHOYA_PRICE = (
        (1, 9),
        (2, 9),
        (3, 9),
        (4, 0),
    )
    GREEN_TEA = (
        (1, "1 cup"),
        (2, "None"),
    )

    GRREN_TEA_PRICE = (
        (1, 3),
        (2, 0)
    )
    WATER = (
        (1, "1 cup"),
        (2, "None"),
    )

    WATER_PRICE =(
        (1, 0),
        (2, 0),
    )
    price = models.DecimalField(
        max_digits=100, decimal_places=2, default=00.00, null=True, blank=True)  # 22.12
    sake = models.IntegerField(
        choices=SAKE, default=1)
    beer = models.IntegerField(choices=BEER, default=1)
    choya = models.IntegerField(choices=CHOYA, default=1)
    green_tea = models.IntegerField(choices=GREEN_TEA, default=1)
    water = models.IntegerField(choices=WATER, default=1)
    # customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    
    @property
    def sake_choice(self):
        return self.SAKE[self.sake-1][1]
    
    @property
    def beer_choice(self):
        return self.BEER[self.beer-1][1]
    
    @property
    def choya_choice(self):
        return self.CHOYA[self.choya-1][1]
    
    @property
    def green_tea_choice(self):
        return self.GREEN_TEA[self.green_tea-1][1]
    
    @property
    def water_choice(self):
        return self.WATER[self.water-1][1]
    
    def save(self, *args, **kwargs):
        price = self.SAKE_PRICE[self.sake-1][1] + self.BEER_PRICE[self.beer-1][1] + self.CHOYA_PRICE[self.choya-1][1] + self.GREEN_TEA_PRICE[self.green_tea-1][1] + self.WATER_PRICE[self.water-1][1]
        self.price = decimal.Decimal(price)

        super(Drink, self).save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ramen = models.ForeignKey(
        Ramen, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    sushi = models.ForeignKey(
        Sushi, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    drink = models.ForeignKey(
        Drink, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True, null=True)
    def save(self, *args, **kwargs):
        self.total_price = 0
        if self.sushi:
            self.total_price += self.sushi.price
        if self.drink:
            self.total_price += self.drink.price
        if self.ramen:
            self.total_price += self.ramen.price
        super().save(*args, **kwargs)
    
      


class Confirm(models.Model):
    your_name = models.CharField(max_length=100)
    dinning_time = models.TimeField(auto_now=False, auto_now_add=False)
    arriving_date = models.DateField(auto_now=False, auto_now_add=False)
    number_of_people = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    email = models.EmailField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):

        super(Confirm, self).save(*args, **kwargs)
