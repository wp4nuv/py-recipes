from django.db import models


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    instructions = models.CharField(max_length=5000)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=50)