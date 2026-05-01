from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name", "country", "prep_time_min", "cook_time_min",
            "serves", "spice_level", "prep_complexity", "source_url"
        ]
class FilterForm(forms.Form):
    country = forms.ChoiceField(required=False)
    min_serves = forms.IntegerField(required=False, min_value=1, label="Min serves")
    max_serves = forms.IntegerField(required=False, min_value=1, label="Max serves")
    min_spice = forms.IntegerField(required=False, min_value=1, max_value=5, label="Min spice")
    max_spice = forms.IntegerField(required=False, min_value=1, max_value=5, label="Max spice")
    max_prep = forms.IntegerField(required=False, min_value=0, label="Max prep (min)")
    max_cook = forms.IntegerField(required=False, min_value=0, label="Max cook (min)")
