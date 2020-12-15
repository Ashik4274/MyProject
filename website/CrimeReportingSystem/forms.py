from django import forms
from .import models

class AddCrimes(forms.ModelForm):
    class Meta:
        model = models.Crimelist
        fields = ['crimename', 'cdes']
