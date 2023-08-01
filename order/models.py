from django.db import models

# Create your models here.


class Ramen(models.Model):
    INGREDIENT_CHOICES = (
        (1, "Egg"),
        (2, "Chicken"),
        (3, "Pork"),
    )

    SIDE_DISH_CHOICES = (
        (1, "Pork dumpling"),
        (2, "Beef dumpling"),
    )

    SOUP_CHOICES = (
        (1, "Beef soup"),
        (2, "Pork soup"),
    )

    NOODLE_CHOICES = (
        (1, "One"),
        (2, "Two"),
    )

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=10.00)  # 22.12
    ingredient_choice = models.IntegerField(
        choices=INGREDIENT_CHOICES, default=1)
    side_dish = models.IntegerField(choices=SIDE_DISH_CHOICES, default=1)
    soup_choice = models.IntegerField(choices=SOUP_CHOICES, default=1)
    noodle_choice = models.IntegerField(choices=NOODLE_CHOICES, default=1)

    def __str__(self) -> str:
        return "RAMEN"

    def save(self, *args, **kwargs):
        if self.ingredient_choice == 1:
            self.price = decimal.Decimal(12)
        if self.ingredient_choice == 2:
            self.price = decimal.Decimal(13)
        if self.ingredient_choice == 3:
            self.price = decimal.Decimal(14)
        super(Ramen, self).save(*args, **kwargs)


class Sushi(models.Model):
    NIGIRI_SUSHI = (
        (1, "raw Salmon"),
        (2, "raw Tuna"),
        (3, "shrimp"),
        (4, "sea urchin (Uni)"),
        (5, "Ikura"),
        (6, "Amberjack"),
        (7, "None"),

    )

    INARI_SUSHI = (
        (1, "Inari Sushi"),
        (2, "None"),

    )

    MAKI_SUSHI = (
        (1, "6 with 3 kinds of fish salmon, tuna, amberjack"),
        (2, "6 with cucumber, carrot and egg"),
        (3, "6 with sesame topping, cucumber, egg and crab stick inside"),
        (4, "None")
    )

    TEMAKI_SUSHI = (
        (1, " with Crab Stick, carrot and cucumber"),
        (2, "With shrimp and cucumber"),
        (3, "With Ikura, egg, and salad vegetables"),
        (4, "With salmon"),
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
        if self.INAKI_SUSHI >= 6:
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