from django.contrib import admin
from .models import Libro, Contacto, Registro, About, Consulta

# Register your models here.

admin.site.register(Libro)
admin.site.register(Contacto)
admin.site.register(Registro)
admin.site.register(About)
admin.site.register(Consulta)


