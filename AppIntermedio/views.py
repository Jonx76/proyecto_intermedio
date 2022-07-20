from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.http import HttpResponse


# Create your views here.



def libros(request):
    libros = Libro.objects.all()
    return render(request,"libros/index.html", {'libros': libros})

def inicio(request):
    return render(request,"AppIntermedio/inicio.html")

def crear(request):
    formulario = LibroForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,"libros/crear.html", {'formulario': formulario})

def editar(request):
    return render(request,"libros/editar.html")

def ubicacion(request):
    return render(request, "ubicacion/buscar.html")

def buscar(request):
    return render(request, "ubicacion/buscar.html")

def contacto(request):
    return render(request, "contacto/contacto.html")

def datoscontacto(request):
    return render(request, "contacto/contacto.html")
