from django import forms
from .models import Viewmap

class Viewform(forms.ModelForm):
    class Meta:
        model = Viewmap
        fields = '__all__'