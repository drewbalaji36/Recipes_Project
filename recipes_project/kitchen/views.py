from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm, FilterForm

def list_recipes(request):
    qs = Recipe.objects.all()
    countries = Recipe.objects.values_list("country", flat=True).distinct().order_by("country")
    country_choices = [("", "— Any Country —")] + [(c, c) for c in countries]

    if request.GET:
        form = FilterForm(request.GET)
        form.fields["country"].choices = country_choices
        if form.is_valid():
            cd = form.cleaned_data
            if cd.get("country"):
                qs = qs.filter(country=cd["country"])
            if cd.get("min_serves") is not None:
                qs = qs.filter(serves__gte=cd["min_serves"])
            if cd.get("max_serves") is not None:
                qs = qs.filter(serves__lte=cd["max_serves"])
            if cd.get("min_spice") is not None:
                qs = qs.filter(spice_level__gte=cd["min_spice"])
            if cd.get("max_spice") is not None:
                qs = qs.filter(spice_level__lte=cd["max_spice"])
            if cd.get("max_prep") is not None:
                qs = qs.filter(prep_time_min__lte=cd["max_prep"])
            if cd.get("max_cook") is not None:
                qs = qs.filter(cook_time_min__lte=cd["max_cook"])
    else:
        form = FilterForm()
        form.fields["country"].choices = country_choices

    return render(request, "kitchen/recipe_list.html", {"form": form, "recipes": qs})

def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes:list")
    else:
        form = RecipeForm()
    return render(request, "kitchen/recipe_form.html", {"form": form, "title": "Add Recipe"})

def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "kitchen/recipe_form.html", {"form": form, "title": f"Edit: {recipe.name}"})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:list")
    return render(request, "kitchen/recipe_confirm_delete.html", {"recipe": recipe})
