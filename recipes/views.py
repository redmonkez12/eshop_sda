from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

from recipes.forms import RecipeForm


def index(request):
    recipe_form = RecipeForm()
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = User.objects.filter(id=1).first()
            recipe.save()
            messages.success(request, 'Your recipe has been saved.')

    return render(request, "dashboard/index.html", {"form": recipe_form})