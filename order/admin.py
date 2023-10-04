from django.contrib import admin
from .models import Ramen, Sushi, Drink, Order, Confirm
# Register your models here.

class RamenAdmin (admin.ModelAdmin):
    list_display = ("customer", "toppings_choice", "side_dish", "soup_choice", "order_time") 
    list_filter = ("order_time", "toppings_choice", "side_dish", "soup_choice")
admin.site.register(Ramen, RamenAdmin)

class SushiAdmin (admin.ModelAdmin):
    list_display = ("customer", "order_time") 
    list_filter = ("order_time",)
admin.site.register(Sushi, SushiAdmin)

class DrinkAdmin (admin.ModelAdmin):
    list_display = ("customer", "order_time") 
    list_filter = ("order_time", )
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Order)
admin.site.register(Confirm)
