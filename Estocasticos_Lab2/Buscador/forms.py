from django import forms
from .models import Paginas

# Aca van los formularios

class Escoger(forms.Form):
    tenis = forms.CharField(max_length=10, label='Tenis')
    