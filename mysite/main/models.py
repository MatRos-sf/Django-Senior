from django.db import models
from django.urls import reverse
# Create your models here.

class ListaZakupow(models.Model):
    lista = models.TextField()
    miejscowosc = models.CharField(max_length=100)
    adres = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    email = models.EmailField(null = True, blank = True)
    imie = models.CharField(max_length=15)
    nazwisko = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)
    aktywne = models.BooleanField(null=True, default=True )
    realizacja = models.BooleanField(null=True,  default=False)


    def get_absolute_url(self):
        return reverse('home')