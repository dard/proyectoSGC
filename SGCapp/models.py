from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from SGC.settings import MEDIA_URL, STATIC_URL
from django.conf import settings

# Create your models here.


class Caja(models.Model):
    ESTADO_ABIERTO = 'A'
    ESTADO_CERRADO = 'C'

    ESTADO_OPCIONES = (
        (ESTADO_ABIERTO, 'Abierta'),
        (ESTADO_CERRADO, 'Cerrada')
    )

    user_caja = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  verbose_name='usuario caja', related_name='user_caja')
    estado = models.CharField(max_length=1, choices=ESTADO_OPCIONES)
    fecha_cierre = models.DateTimeField(auto_now=True, verbose_name='fecha cierre')
    saldo_inicial = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='saldo inicial')
    monto_cierre = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='monto cierre')

    def __str__(self):
        return '{} {} {} {} {}'.format(self.pk, self.user_caja, self.fecha_cierre, self.saldo_inicial, self.monto_cierre)

    class Meta:
        ordering = ['id']


class Cliente (models.Model):

    nombre = models.CharField(max_length=25, null=True, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=25, null=True, blank=True, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='Dni')
    telefono = models.IntegerField(verbose_name='Telefono')
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=40, null=True, blank=True, verbose_name='Dirección')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.nombre, self.apellido, self.dni, self.telefono, self.email,  self.creado)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Cobrador (models.Model):
    #    user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                             null=True, related_name='userCobrador')
    nombre = models.CharField(max_length=25, null=True, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=25, null=True, blank=True, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='Dni')
    telefono = models.IntegerField(verbose_name='Telefono', null=True)
    direccion = models.CharField(max_length=40, null=True,
                                 blank=True, verbose_name='Dirección')
    email = models.EmailField(blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.nombre, self.apellido, self.dni, self.telefono, self.email,  self.creado)

    def toJSON(self):
        item = model_to_dict(self, exclude=['creado', 'actualizado'])
        return item

    class Meta:
        verbose_name = 'Cobrador'
        verbose_name_plural = 'Cobradores'
        ordering = ['id']


class Planilla (models.Model):
    planilla_caja = models.ForeignKey(Caja, on_delete=models.CASCADE, verbose_name='caja')
    planilla_cobrador = models.ForeignKey(
        Cobrador, on_delete=models.CASCADE, verbose_name='cobrador')
    fecha_emision = models.DateTimeField(auto_now_add=True, verbose_name='fecha emision')
    fecha_cierre = models.DateTimeField(auto_now=False)
    monto_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto Total')
    estado = models.CharField(max_length=10, verbose_name='Estado')
    cantidad_recibos = models.IntegerField(verbose_name='Cantidad de Recibos')

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.pk, self.planilla_caja, self.planilla_cobrador, self.fecha_emision, self.fecha_cierre, self.monto_total, self.estado, self.cantidad_recibos)

    class Meta:
        verbose_name = 'Planilla'
        verbose_name_plural = 'Planillas'
        ordering = ['id']


class Recibo(models.Model):
    recibo_planilla = models.ForeignKey(Planilla, on_delete=models.CASCADE, verbose_name='Planilla')
    recibo_caja = models.ForeignKey(Caja, on_delete=models.CASCADE, verbose_name='Caja')
    recibo_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cliente')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    estado = models.CharField(max_length=10, verbose_name='Estado')
    comprobantes_Cancelados = models.CharField(
        max_length=10, verbose_name='Comprobantes Cancelados')
    monto_comprobantes = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Monto Comprobantes')
    medios_de_pago = models.CharField(max_length=10, verbose_name='Medios de Pago')

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format(self.recibo_caja, self.recibo_cliente, self.monto, self.fecha, self.estado, self.comprobantes_Cancelados, self.monto_comprobantes, self.medios_de_pago)

    class Meta:
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
        ordering = ['id']


class Comprobante (models.Model):
    comprobante_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cliente')
    fecha_comprobante = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    monto_original = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto')
    monto_cancelado = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Monto Cancelado')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} {} {} {} {}'.format(self.comprobante_cliente, self.cliente, self.fecha_comprobante, self.monto_original, self.monto_cancelado)


class ComprobanteGenerado (models.Model):
    comprobante_recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE, verbose_name='Recibo')
    comprobante_generado = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE, verbose_name='Comprobante')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} {} {} {}'.format(self.pk, self.comprobante_recibo, self.comprobante_generado, self.monto)


class Anticipo (models.Model):
    anticipo_recibo = models.ForeignKey(
        Recibo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Recibo')
    anticipo_comprobante = models.ForeignKey(
        Comprobante, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Comprobante')
    monto = models.DecimalField(max_digits=8, decimal_places=2,
                                null=True, blank=True, verbose_name='Monto')

    class Meta:
        verbose_name = 'Anticipo'
        verbose_name_plural = 'Anticipos'
        ordering = ['id']

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return '{} {} {}' .format(self.anticipo_recibo, self.anticipo_comprobante, self.monto)


class Banco (models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    def __str__(self):
        return '{}'.format(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['id']


class Cheque (models.Model):
    cheque_banco = models.ForeignKey(
        Banco, on_delete=models.CASCADE, verbose_name='Banco')
    # cheque_recibo = models.ForeignKey(
    #     Recibo, on_delete=models.CASCADE, verbose_name='Recibo', null=True, blank=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0,
                                 unique=True, verbose_name='Numero Cheque')
    monto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Monto')
    imagen = models.ImageField(upload_to='cheque/%Y/%m/%d', null=True, blank=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        else:
            return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_imagen()  # Parseo el campo imagen
        return item

    def __str__(self):
        return '{} {} {} {}'.format(self.cheque_banco, self.numero, self.monto, self.imagen)

    class Meta:
        verbose_name = 'Cheque'
        verbose_name_plural = 'Cheques'
        ordering = ['id']
