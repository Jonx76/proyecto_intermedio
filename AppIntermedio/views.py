from django.shortcuts import render, redirect
from .models import Consulta, Libro, Registro
from .forms import ConsultaForm, LibroForm, RegistroForm, ConsultaForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.



class LibroList(ListView):
    model = Libro
    context_object_name = "libros"
    template_name = "Libros\index.html"

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

def contacto(request):
    return render(request, "contacto/contacto.html")

def datoscontacto(request):
    return render(request, "contacto/contacto.html")

def registro(request):
    registro = Registro.objects.all()
    return render(request,"registro/registro.html", {'registro': registro})

def crearsocio(request):
    formulario = RegistroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registro')
    return render(request,"registro/crearsocio.html", {'formulario': formulario})

def about(request):
    return render(request, "about/about.html")

def aboutus(request):
    pass
    
def consulta(request):
    consulta = Consulta.objects.all()
    return render(request, "consulta/consulta.html", {"consulta": consulta})    

def crearconsulta(request):
    formulario = ConsultaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('consulta')
    return render(request,"consulta/crearconsulta.html", {'formulario': formulario})

class LibroDetalle(DetailView):
    model = Libro
    context_object_name = "libros"
    template_name = "Libros\detalle.html"
    fields= "__all__"

#-------- Seccion Ingreso    
class PanelLogin(LoginView):
    template_name = 'ingreso/login.html'
    next_page = reverse_lazy("inicio")

class PanelLogout(LogoutView):
    template_name = 'ingreso/logout.html'

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'ingreso/crear_cuenta_form.html'
  success_url = reverse_lazy('inicio')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

def eliminar(request, titulo):
    libro = Libro.objects.get(titulo=titulo)
    libro.delete()  
    return redirect('libros')