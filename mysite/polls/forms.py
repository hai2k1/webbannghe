from django import forms
from .models import donhang

class Form(forms.ModelForm):
    
    class Meta:
        model = donhang
        fields = ("",)
    