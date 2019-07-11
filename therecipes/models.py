from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    instructions = models.CharField(max_length=5000)

class RecipeIngredient(models.Model):
    recipe

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)