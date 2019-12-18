from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=20)
    imagen = models.FilePathField(path="/img")
