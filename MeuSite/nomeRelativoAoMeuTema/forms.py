from django import forms
from .models import MTCars

class MTCarsForm(forms.ModelForm):
    class Meta:
        model = MTCars
        fields = '__all__'
