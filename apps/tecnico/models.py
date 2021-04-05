from django.db import models
from apps.gerente.models import Cliente
from apps.users.models import User
from django.utils.timezone import now
# Create your models here.

class OrdenTrabajo(models.Model):
    equipo = models.CharField(max_length=100,blank=True)
    marca = models.CharField(max_length=100,blank=True)
    modelo = models.CharField(max_length=100,blank=True)
    descripcion = models.CharField(max_length=255,blank=True)
    nroSerie = models.CharField(max_length=100,blank=True)
    fechaIngreso = models.DateTimeField(default=now, blank=True)
    estadoEquipo = models.CharField(max_length=100,blank=True)
    fechaEstEqui = models.CharField(max_length=100,blank=True)
    estadoPresupuesto = models.CharField(max_length=100,blank=True)
    fechaEstPresu = models.CharField(max_length=100,blank=True)
    tecnico = models.ForeignKey(
        User, null=True,blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, null=True,blank=True, on_delete=models.CASCADE)


class TareasOT(models.Model):
    ot = models.ForeignKey(OrdenTrabajo, null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    idProducto = models.IntegerField()
    cantidad = models.IntegerField()
