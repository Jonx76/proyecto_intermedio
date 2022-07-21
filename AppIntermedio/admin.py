from django.contrib import admin
from .models import Libro, Ubicacion, Contacto, Registro, About

# Register your models here.

admin.site.register(Libro)
admin.site.register(Ubicacion)
admin.site.register(Contacto)
admin.site.register(Registro)
admin.site.register(About)

