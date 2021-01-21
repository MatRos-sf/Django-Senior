from django import forms
from .models import ListaZakupow

class LisatZakupowForms(forms.ModelForm):

    class Meta:
        model = ListaZakupow
        fields = [
            'imie',
            'nazwisko',
            'miejscowosc',
            'adres',
            'telefon',
            'email',
            'lista'
        ]
