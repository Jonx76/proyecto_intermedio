from django.shortcuts import render, redirect
from .models import  Libro, Registro
from .forms import  ConsultaForm, LibroForm, RegistroForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin



# Create your views here.



class LibroList(ListView):
    model = Libro
    context_object_name = "libros"
    template_name = "Libros\index.html"

def inicio(request):
    return render(request,"AppIntermedio/inicio.html")

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html', {'formulario': formulario})

def editar(request, titulo):
    libro = Libro.objects.get(titulo=titulo)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,"libros/editar.html", {'formulario': formulario})

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

def eliminarregistro(request, nombre):
    registro = Registro.objects.get(nombre=nombre)
    registro.delete()  
    return redirect('registro')

#--------- Seccion CONSULTAS    

def consulta(request):
    data= {
        "form": ConsultaForm()

    }

    if request.method =="POST":
        formulario = ConsultaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Consulta enviada con exito!"
        else:
            data["form"] = formulario    
    return render(request, "Consulta/consulta.html", data)

class perfilusuario(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = User
    template_name = "Usuario\detalle_usuario.html"
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class Actualizar_usuario(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "Usuario/usuario_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("detalleusuario", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])