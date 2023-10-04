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
         max_digits=5, decimal_places=2, default=10.00, null=True, blank=True)  # 22.12
    toppings_choice = models.IntegerField(
        choices=TOPPINGS_CHOICES, default=3)
    side_dish = models.IntegerField(choices=SIDE_DISH_CHOICES, default=1)
    soup_choice = models.IntegerField(
        choices=SOUP_CHOICES, default=1)
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)


    # def __str__(self) -> str:
    #     return "RAMEN"

    def save(self, *args, **kwargs):
        self.price = 0
        if self.toppings_choice == 1:
            if self.soup_choice == 1:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 2:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(9)
            if self.soup_choice == 3:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 4:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(9)
            if self.soup_choice == 5:
                self.price = decimal.Decimal(0)
        if self.toppings_choice == 2:
            if self.soup_choice == 1:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 2:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(9)
            if self.soup_choice == 3:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 4:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 5:
                self.price = decimal.Decimal(0)
        if self.toppings_choice == 3:
            if self.soup_choice == 1:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 2:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(9)
            if self.soup_choice == 3:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 4:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 5:
                self.price = decimal.Decimal(0)
        if self.toppings_choice == 4:
            if self.soup_choice == 1:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 2:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(9)
            if self.soup_choice == 3:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(6)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 4:
                if self.side_dish == 7:
                    self.price = decimal.Decimal(5)
                else:
                    self.price = decimal.Decimal(10)
            if self.soup_choice == 5:
                self.price = decimal.Decimal(0)
        if self.toppings_choice == 5:
            self.price = decimal.Decimal(0)
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
        max_digits=5, decimal_places=2, default=10.00, null=True, blank=True)  # 22.12
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
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self) -> str:
    #     return "SUSHI"

    def save(self, *args, **kwargs):
        self.price = 0
        if self.NIGIRI_SUSHI == 1:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(11)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(5)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                    
        if self.NIGIRI_SUSHI == 2:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(11)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(5)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                    
        if self.NIGIRI_SUSHI == 3:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(12)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(6)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                    
        if self.NIGIRI_SUSHI == 4:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(13)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(28)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(7)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(16)
                    else: 
                        self.price = decimal.Decimal(22)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(16)
                    else: 
                        self.price = decimal.Decimal(22)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(16)
                    else: 
                        self.price = decimal.Decimal(22)
                    
        if self.NIGIRI_SUSHI == 5:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(11)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(20)
                    else:
                        self.price = decimal.Decimal(26)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(5)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(14)
                    else: 
                        self.price = decimal.Decimal(20)
                    
        if self.NIGIRI_SUSHI == 6:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(12)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(27)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(6)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else: 
                        self.price = decimal.Decimal(21)
                    
        if self.NIGIRI_SUSHI == 7:
            if self.INARI_SUSHI == 1:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(6)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(21)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(21)
            if self.INARI_SUSHI == 2:
                if self.MAKI_SUSHI == 4:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(0)
                elif self.MAKI_SUSHI == 1:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(9)
                    else: 
                        self.price = decimal.Decimal(15)
                elif self.MAKI_SUSHI == 2:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(9)
                    else: 
                        self.price = decimal.Decimal(15)
                elif self.MAKI_SUSHI == 3:
                    if self.TEMAKI_SUSHI == 5:
                        self.price = decimal.Decimal(9)
                    else: 
                        self.price = decimal.Decimal(15)
                    
        super(Sushi, self).save(*args, **kwargs)


class Drink(models.Model):
    SAKE = (
        (1, "1 bottle Dassai Sake"),
        (2, "1 bottle Kubota Sake"),
        (3, "1 bottle Yamamoto Sake"),
        (4, "1 bottle Juyondai Sake"),
        (5, "None"),
    )
    BEER = (
        (1, "1 bottle Asahi Super Dry"),
        (2, "1 bottle Saporro Premium"),
        (3, "1 bottle Echigo Koshihikari"),
        (4, "1 bottle Orion Premium Draft Beer"),
        (5, "None"),
    )
    CHOYA = (
        (1, "1 bottle original favor"),
        (2, "1 bottle hoeny favor"),
        (3, "1 bottle peach favor"),
        (4, "None"),
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
        max_digits=100, decimal_places=2, default=00.00, null=True, blank=True)  # 22.12
    SAKE = models.IntegerField(
        choices=SAKE, default=1)
    BEER = models.IntegerField(choices=BEER, default=1)
    CHOYA = models.IntegerField(choices=CHOYA, default=1)
    GREEN_TEA = models.IntegerField(choices=GREEN_TEA, default=1)
    WATER = models.IntegerField(choices=WATER, default=1)
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    order_time = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self) -> str:      
    #     return "DRINK"

    def save(self, *args, **kwargs):
        self.price = 0
        if self.SAKE == 1:
            if self.CHOYA == 4:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(22)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(18)
                    else:
                        self.price = decimal.Decimal(25)
            elif self.CHOYA == 1:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(27)
                    else:
                        self.price = decimal.Decimal(34)
            elif self.CHOYA == 2:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(27)
                    else:
                        self.price = decimal.Decimal(34)
            elif self.CHOYA == 3:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(27)
                    else:
                        self.price = decimal.Decimal(34)

        if self.SAKE == 2:
            if self.CHOYA == 4:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(12)
                    else:
                        self.price = decimal.Decimal(19)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(22)
            elif self.CHOYA == 1:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
            elif self.CHOYA == 2:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
            elif self.CHOYA == 3:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
        
        if self.SAKE == 3:
            if self.CHOYA == 4:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(12)
                    else:
                        self.price = decimal.Decimal(19)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(15)
                    else:
                        self.price = decimal.Decimal(22)
            elif self.CHOYA == 1:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
            elif self.CHOYA == 2:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
            elif self.CHOYA == 3:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(21)
                    else:
                        self.price = decimal.Decimal(28)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(24)
                    else:
                        self.price = decimal.Decimal(31)
        if self.SAKE == 4:
            if self.CHOYA == 4:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(13)
                    else:
                        self.price = decimal.Decimal(20)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(16)
                    else:
                        self.price = decimal.Decimal(23)
            elif self.CHOYA == 1:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(29)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(25)
                    else:
                        self.price = decimal.Decimal(32)
            elif self.CHOYA == 2:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(29)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(25)
                    else:
                        self.price = decimal.Decimal(32)
            elif self.CHOYA == 3:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(22)
                    else:
                        self.price = decimal.Decimal(29)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(25)
                    else:
                        self.price = decimal.Decimal(32)
        
        if self.SAKE == 5:
            if self.CHOYA == 4:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(0)
                    else:
                        self.price = decimal.Decimal(7)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(3)
                    else:
                        self.price = decimal.Decimal(10)
            elif self.CHOYA == 1:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(9)
                    else:
                        self.price = decimal.Decimal(16)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(12)
                    else:
                        self.price = decimal.Decimal(19)
            elif self.CHOYA == 2:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(9)
                    else:
                        self.price = decimal.Decimal(16)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(12)
                    else:
                        self.price = decimal.Decimal(19)
            elif self.CHOYA == 3:
                if self.GREEN_TEA == 2:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(9)
                    else:
                        self.price = decimal.Decimal(16)
                elif self.GREEN_TEA == 1:
                    if self.BEER == 5:
                        self.price = decimal.Decimal(12)
                    else:
                        self.price = decimal.Decimal(19)
        super(Drink, self).save(*args, **kwargs)


class Order(models.Model):
    ramen = models.ForeignKey(
        Ramen, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    sushi = models.ForeignKey(
        Sushi, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    drink = models.ForeignKey(
        Drink, related_name="orders", on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00, null=True, blank=True)
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

    def save(self, *args, **kwargs):

        super(Confirm, self).save(*args, **kwargs)
