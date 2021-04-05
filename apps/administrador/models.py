from django.db import models
from apps.tecnico.models import OrdenTrabajo
from apps.gerente.models import Cliente
from apps.users.models import User
from django.utils.timezone import now
from decimal import Decimal
# Create your models here.


class Remito(models.Model):
    oti = models.OneToOneField(
        OrdenTrabajo, null=True, blank=True, on_delete=models.CASCADE)
    fechaIngreso = models.DateTimeField(default=now, blank=True)
    administrador = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    informacion = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)

class Factura(models.Model):
    oti = models.OneToOneField(
        OrdenTrabajo, null=True, blank=True, on_delete=models.CASCADE)
    fechaIngreso = models.DateTimeField(default=now, blank=True)
    administrador = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    informacion = models.CharField(max_length=255, blank=True)
    importe = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))