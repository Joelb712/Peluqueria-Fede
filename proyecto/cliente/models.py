from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Cliente(models.Model):
    id_cliente= models.AutoField(primary_key=True , editable=False)
    nombre_cliente=models.CharField(verbose_name='nombre', max_length=100, blank=False)
    apellido_cliente=models.CharField(verbose_name='apellido',max_length=100,blank=False)
    telefono_cliente=models.CharField(verbose_name='telefono',  max_length=20,unique=True, blank=False )
    correo_cliente=models.EmailField(verbose_name='correo',  unique=True , blank=False)
    fecha_nacimiento_cliente= models.DateField(verbose_name='fecha De Nacimiento', blank=True , null=True)
    
    def __str__(self):
        return f'{self.nombre_cliente} {self.apellido_cliente}'
    
    class Meta:
        db_table='clientes'