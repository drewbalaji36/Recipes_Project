from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    prep_time_min = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    cook_time_min = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    serves = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    spice_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    prep_complexity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    source_url = models.URLField(null=True, blank=True, help_text="Link to the recipe page (optional)")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.country})"
