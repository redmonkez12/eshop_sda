from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    label = models.CharField(max_length=200)
    duration = models.DecimalField(decimal_places=2, max_digits=10)
    portion = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Difficulty(models.Model):
    class DifficultyChoices(models.TextChoices):
        EASY = "ES", "EASY"
        MEDIUM = "ME", "MEDIUM"
        HARD = "HA", "HARD"

    label = models.CharField(max_length=2, choices=DifficultyChoices, unique=True)


class Unit(models.Model):
    label = models.CharField(max_length=50)


class IngredientGroup(models.Model):
    label = models.CharField(max_length=200)


class Ingredient(models.Model):
    label = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    note = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    ingredient_group = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE, null=True, blank=True)
