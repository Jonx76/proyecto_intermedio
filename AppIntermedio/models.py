from django.db import models

# Create your models here.

class Libro(models.Model):
    ## id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción",null=True)

    def __str__(self):  
        fila = "Titulo: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.imagen.name)
        super().delete()

#class autor

class Ubicacion(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    def __str__(self):
        fila = "Titulo: " + self.titulo
        return fila

class Contacto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    def __str__(self):
        fila = "Titulo: " + self.titulo
        return fila

class Registro(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='NOMBRE')
    apellido = models.CharField(max_length=100, verbose_name='APELLIDO')
    telefono = models.IntegerField(verbose_name='TELEFONO DE CONTACTO')
    email = models.EmailField(verbose_name="E-MAIL")
    def __str__(self):
        fila = "NOMBRE: " + self.nombre + " - " + "APELLIDO: " + self.apellido +  " - " + "E-MAIL: " + self.email
        return fila
        
    def __int__(self):
        fila2 ="Telefono de contacto" + self.telefono
        return fila2