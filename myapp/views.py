from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm, SearchForm, RegistroForm

def index(request):
    libros = Libro.objects.all()
    return render(request, 'index.html', {'libros': libros})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor agregado exitosamente.')
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = form.save(commit=False)
            autor, created = Autor.objects.get_or_create(
                name=request.user.username,
                defaults={'email': request.user.email}
            )
            libro.author = autor
            libro.save()
            messages.success(request, 'Libro agregado exitosamente.')
            return redirect('index')
    else:
        form = LibroForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def add_publisher(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editorial agregada.')
            return redirect('index')
    else:
        form = EditorialForm()
    return render(request, 'add_publisher.html', {'form': form})

@login_required
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if libro.author.name != request.user.username:
        messages.error(request, 'No tienes permiso para editar este libro.')
        return redirect('index')
    
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro editado exitosamente!')
            return redirect('libro_listado')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form})

@login_required
def borrar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'GET':
        if libro.author.email != request.user.email:
            return HttpResponseForbidden('No tenes permiso para eliminar este libro.')
        return render(request, 'borrar_libro.html', {'libro': libro})
    elif request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado con éxito.')
        return redirect('index')

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Libro.objects.filter(title__icontains=query)
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Has sido logueado.')
            return redirect('registro_exitoso')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registration/registro_exitoso.html')

def libro_listado(request):
    libros = Libro.objects.all()
    return render(request, 'libro_listado.html', {'libros': libros})

def acerca_de(request):
    return render(request, 'acerca_de.html')
