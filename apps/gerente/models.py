from django.db import models

# Create your models here.
class EquipoMarca(models.Model):
    nombreMarca = models.CharField(max_length=100, unique=True)


class EquipoModel(models.Model):
    nombreModel = models.CharField(max_length=100, unique=True)
    marca =models.ForeignKey(EquipoMarca, null= True, blank= True, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pago = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100,blank=True)
    domicilio = models.CharField(max_length=100,blank=True)

class Stock(models.Model):
    nombreCategoria = models.CharField(max_length=100, unique=True)

class Productos(models.Model):
    categoria = models.ForeignKey(Stock, null= True, blank= True, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    nroSerie = models.CharField(max_length=100)

class EquipoBackup(models.Model):
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    nroSerie = models.CharField(max_length=100, unique=True)
    cliente = models.ForeignKey(Cliente, null= True, blank= True, on_delete=models.CASCADE)
    ordenTrabajo = models.ForeignKey('tecnico.OrdenTrabajo', null= True, blank= True, on_delete=models.CASCADE)