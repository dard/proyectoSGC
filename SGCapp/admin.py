from django.contrib import admin
from SGCapp.models import *

# Register your models here.
'''
@admin.register(User)
class UserAdmin(AbstractUser):
    list_display = ('nombre','apellido', 'dni', 'telefono', 'email', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'
'''


class CobradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'telefono',
                    'email', 'direccion', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'telefono',
                    'email', 'direccion', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'


# @admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('user_caja', 'estado', 'fecha_cierre', 'saldo_inicial', 'monto_cierre')

# @admin.register(Planilla)


class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('planilla_caja', 'planilla_cobrador', 'fecha_emision',
                    'fecha_cierre', 'monto_total', 'estado', 'cantidad_recibos')
    search_fields = ('planilla_caja', 'planilla_cobrador')
    list_filter = ('estado',)
    date_hierarchy = 'fecha_emision'

# @admin.register(Comprobante)


class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('fecha_comprobante', 'monto_original', 'monto_cancelado')
    search_fields = ('monto_original', 'monto_cancelado')
    date_hierarchy = 'fecha_comprobante'

# @admin.register(ComprobanteGenerado)


class ComprobanteGeneradoAdmin(admin.ModelAdmin):
    list_display = ('comprobante_recibo', 'comprobante_generado', 'monto')
    search_fields = ('comprobante_generado',)
    list_filter = ('monto',)

# @admin.register(Recibo)


class ReciboAdmin(admin.ModelAdmin):
    list_display = ('recibo_planilla', 'recibo_caja', 'monto', 'fecha', 'estado',
                    'comprobantes_Cancelados', 'monto_comprobantes', 'medios_de_pago')
    search_fields = ('pk', 'monto')
    list_filter = ('estado',)
    date_hierarchy = 'fecha'


class AnticipoAdmin(admin.ModelAdmin):
    list_display = ('anticipo_recibo', 'anticipo_comprobante', 'monto')
    search_fields = ('anticipo_comprobante',)
    list_filter = ('monto',)

# @admin.register(Banco)


class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# @admin.register(Cheque)


class ChequeAdmin(admin.ModelAdmin):
    list_display = ('cheque_banco', 'cheque_recibo', 'numero', 'monto')
    search_fields = ('numero',)
    list_filter = ('monto',)


admin.site.register(Cobrador, CobradorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Planilla, PlanillaAdmin)
admin.site.register(Caja, CajaAdmin)
admin.site.register(Comprobante, ComprobanteAdmin)
admin.site.register(ComprobanteGenerado, ComprobanteGeneradoAdmin)
admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Anticipo, AnticipoAdmin)
admin.site.register(Banco, BancoAdmin)
admin.site.register(Cheque, ChequeAdmin)
