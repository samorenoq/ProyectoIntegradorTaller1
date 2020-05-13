from django.db import models
import uuid
# Create your models here.

class Temperature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    latitud = models.IntegerField(verbose_name='Latitud')
    longitud = models.IntegerField(verbose_name='Longitud')
    tipo_terreno = models.CharField(verbose_name='TipoTerreno', max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)