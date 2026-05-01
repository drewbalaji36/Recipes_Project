from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, db_index=True)
    prep_time_min = models.PositiveIntegerField(validators=[MinValueValidator(0)], db_index=True)
    cook_time_min = models.PositiveIntegerField(validators=[MinValueValidator(0)], db_index=True)
    serves = models.PositiveIntegerField(validators=[MinValueValidator(1)], db_index=True)
    spice_level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        db_index=True
    )
    prep_complexity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    source_url = models.URLField(null=True, blank=True, help_text="Link to the recipe page (optional)")  # >>> NEW
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=["country", "serves"]),
            models.Index(fields=["spice_level"]),
            models.Index(fields=["prep_time_min"]),
            models.Index(fields=["cook_time_min"]),
        ]
    def __str__(self):
        return f"{self.name} ({self.country})"
