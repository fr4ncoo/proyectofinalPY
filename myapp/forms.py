from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'email']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['title', 'publication_date', 'author']

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['name', 'address']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
