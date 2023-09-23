from django.db import models

class Smoothie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return f"Smoothie(ID: {self.id}, Name: {self.name}, Description: {self.description})"

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

class SmoothieIngredient(models.Model):
    smoothie = models.ForeignKey(Smoothie, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()  # in grams
