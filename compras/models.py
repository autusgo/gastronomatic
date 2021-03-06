from django.db import models

from django.conf import settings
from decimal import Decimal
from localflavor.ar.forms import ARCUITField
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from model_utils import Choices
from model_utils.fields import MonitorField
from django.utils.translation import ugettext_lazy as _

#PRODUCTOS
class Producto(models.Model):
    UNIDAD_DE_MEDIDA = (
            ('Litro', 'Litro'),
            ('Kilo', 'Kilo'),
            ('Gramo', 'Gramo'),
            ('Cm3', 'Cm3'),
            ('Unidad', 'Unidad'),
            )
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=9 , decimal_places=2)
    unidad_de_medida = models.CharField(max_length=200, null=True, choices=UNIDAD_DE_MEDIDA)
    stock = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ('nombre',)
        index_together = (('tipo', 'nombre'))

    def __str__(self):
        return '{}'.format(self.nombre)
    def __unicode__(self):
        return '{}'.format(self.nombre)

#PROVEEDORES
class Proveedor(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    CUIT = models.CharField(max_length=13)
    teléfono = models.CharField(max_length=10)
    correo_electrónico = models.EmailField(max_length=100)
    dirección = models.CharField(max_length=200)
    deuda = models.DecimalField(max_digits=9 , decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)
    def __unicode__(self):
        return '{} {}'.format(self.apellido, self.nombre)

    #class Meta:
    #    ordering = ['producto']

#FACTURAS
class Factura(models.Model):
    ESTADO = (
            ('PAGA', 'PAGA'),
            ('IMPAGA', 'IMPAGA'),
            )
    # TIPO = (
    #         ('Factura A', 'Factura A'),
    #         ('Factura B', 'Factura B'),
    #         ('Factura C', 'Factura C'),
    #         )

    fecha = models.DateField(default=datetime.date.today)
    numero = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    #productos = models.ManyToManyField(Producto, null=True, blank=True)
    #detalle = models.ForeignKey(Detalle, null=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200, choices=ESTADO, default='IMPAGA')
    fecha_de_pago = MonitorField(monitor='estado', when=['PAGA'], verbose_name=_(u'Fecha de pago'), blank=True, null=True, default=None)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    # tipo = models.CharField(max_length=200, choices=TIPO)

    class Meta:
        ordering = ('estado',)
        index_together = (('proveedor', 'estado'))

    # def total_detalles(self):
    #     total_detalles = self.detalle.total_linea
    #     return round(total_detalles, 2)

    def __str__(self):
        return '{} {} {}'.format(self.numero, self.proveedor.apellido, self.estado)
    def __unicode__(self):
        return '{} {} {}'.format(self.numero, self.proveedor.apellido, self.estado)

#DETALLE
class Detalle(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def total_linea(self):
        total_linea = round(self.producto.precio_unitario * self.cantidad, 2)
        return round(total_linea, 2)

    def total_detalle(self, factuid):
        total_detalle = 0
        for det in Detalle.objects.filter(factura=factuid):
            total_detalle += self.subtotal
        return round(total_detalle, 2)


    def __unicode__(self):
        return '{} {} {}'.format(self.cantidad, self.producto.nombre, self.total_linea)
