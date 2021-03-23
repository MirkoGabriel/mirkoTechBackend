from django.db import models
from apps.gerente.models import Cliente 
from apps.users.models import User
# Create your models here.

class OrdenTrabajo(models.Model):
    equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100,null=True)
    nroSerie = models.CharField(max_length=100)
    fechaIngreso= models.DateField(null=False)
    estadoEquipo = models.CharField(max_length=100,null=True)
    fechaEstEqui= models.DateField(null=True)
    estadoPresupuesto = models.CharField(max_length=100,null=True)
    fechaEstPresu= models.DateField(null=True)
    tecnico = models.ForeignKey(User, null= True, blank= True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null= True, blank= True, on_delete=models.CASCADE)
