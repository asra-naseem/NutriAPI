from rest_framework import serializers
from .models import Smoothie, Ingredient, SmoothieIngredient

# Serializer for the Smoothie model
class SmoothieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smoothie
        fields = ['id', 'name', 'description']

# Serializer for the Ingredient model
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'calories', 'protein', 'fat', 'carbs']

# Serializer for the SmoothieIngredient model
class SmoothieIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmoothieIngredient
        fields = ['id', 'smoothie', 'ingredient', 'quantity']
