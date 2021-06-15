from django.db import models
from django.urls import reverse

class Estadio(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    imagen = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.nombre

opciones = [
    [0,"Activo"],
    [1,"No Activo"],
]

class Equipo(models.Model):
    status = models.IntegerField(choices=opciones)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(null=True,blank=True)
    fechaJuego = models.DateTimeField(null=True)
    estadio = models.ForeignKey(
        Estadio,
        null=True,
        blank=True,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.nombre

class Extra(models.Model):
    rival = models.ForeignKey(
        Equipo,
        null=True,
        blank=True,
        on_delete = models.CASCADE,
    )
    historia = models.TextField(max_length=100000)
    uniforme = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.historia

def get_absolute_url(self):
        return reverse('modelos', args=[str(self.id)])