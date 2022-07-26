"""intermedio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppIntermedio.views import inicio, crear, editar, contacto, datoscontacto, crearsocio, registro, about, aboutus, consulta, crearconsulta, LibroList
from AppIntermedio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', views.LibroList.as_view(), name='libros'),
    path("", views.inicio, name='inicio'),
    path('libros/crear', crear, name='crear'),
    path('libros/editar', editar, name='editar'),
    path('contacto/', contacto, name='contacto'),
    path('contacto/datoscontacto', datoscontacto, name='datoscontacto'),
    path('registro/', registro, name='registro'),
    path('registro/crearsocio', crearsocio, name='crearsocio'),
    path('about/', about, name='about'),
    path('about/aboutus', aboutus, name='aboutus'),
    path("consulta/", consulta, name="consulta"),
    path("consulta/crearconsulta", crearconsulta, name="crearconsulta"),


]
