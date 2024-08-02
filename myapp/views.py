from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm, SearchForm

def index(request):
    return render(request, 'index.html')


def add_author(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibroForm()
    return render(request, 'add_book.html', {'form': form})

def add_publisher(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditorialForm()
    return render(request, 'add_publisher.html', {'form': form})

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
