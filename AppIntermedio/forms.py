from django import forms
from .models import Libro, Registro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'