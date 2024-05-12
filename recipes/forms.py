from django import forms

from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    label = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    duration = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    portion = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Recipe
        fields = ("label", "duration", "portion")