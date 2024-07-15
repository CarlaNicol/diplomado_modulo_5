from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria


'''def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    filtro_nombre = request.GET.get("nombre")
    print(filtro_nombre)
    items = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias": items})'''
    
def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        items = Categoria.objects.filter(nombre__icontains=filtro_nombre)
        print(f"Filtrando categorías con nombre que contiene: {filtro_nombre}")
    else:
        items = Categoria.objects.all()
        print("Mostrando todas las categorías")
    print(f"Categorías obtenidas: {items}")
    return render(request, "categorias.html", {"categorias": items})