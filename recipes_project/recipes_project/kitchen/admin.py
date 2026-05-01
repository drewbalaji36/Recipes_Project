from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name", "country", "serves", "spice_level",
        "prep_time_min", "cook_time_min", "prep_complexity",
        "source_url"
    )
    search_fields = ("name", "country")
    list_filter = ("country", "spice_level", "prep_complexity")
