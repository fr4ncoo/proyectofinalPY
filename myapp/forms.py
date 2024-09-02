from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'email']
        labels = {
            'name': 'Nombre',
            'email': 'Correo Electrónico',
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['title', 'publication_date', 'author', 'editorial', 'cover_image']
        labels = {
            'title': 'Título',
            'publication_date': 'Fecha de Publicación',
            'author': 'Autor',
            'editorial': 'Editorial'
        }

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['name', 'address']
        labels = {
            'name': 'Nombre',
            'address': 'Dirección',
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user