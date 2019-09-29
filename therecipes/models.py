from django.db import models

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, default=0)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    instructions = models.CharField(max_length=5000)
 
    def __str__(self):
        return self.recipe_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=50)