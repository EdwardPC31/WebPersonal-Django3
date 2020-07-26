from django.db import models

# Create your models here.

# Creamos una clase
class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name = "Titulo") # <-- Atributo de la tabla o columna 
    descripcion = models.TextField(verbose_name = "Descripcion")
    imagen = models.ImageField(verbose_name = "Imagen", upload_to="Projects")
    link = models.URLField(null=True, blank=True, verbose_name="Dirección Web") # <============ URLField
    creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creacion")
    modificacion = models.DateField(auto_now=True,verbose_name = "Fecha de Modificacion")

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-creacion"]

    def __str__(self):
        return self.titulo
