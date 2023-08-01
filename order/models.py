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

    