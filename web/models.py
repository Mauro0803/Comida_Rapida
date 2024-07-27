from django.db import models

# Create your models here.

class Venta(models.Model):
    local_id = models.IntegerField()
    venta_fecha = models.DateField()
    venta_monto = models.IntegerField()
    venta_cantidad = models.IntegerField()