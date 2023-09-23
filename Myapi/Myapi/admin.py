from django.contrib import admin
from .models import Smoothie,Ingredient,SmoothieIngredient

admin.site.register(Smoothie)
admin.site.register(Ingredient)
admin.site.register(SmoothieIngredient)