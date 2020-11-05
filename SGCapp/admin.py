from django.contrib import admin
from SGCapp.models import *

# Register your models here.
'''
@admin.register(User)
class UserAdmin(AbstractUser):
    list_display = ('id', 'nombre','apellido', 'dni', 'telefono', 'email', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'
'''


class CobradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'telefono',
                    'email', 'direccion', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'telefono',
                    'email', 'direccion', 'creado', 'actualizado')
    search_fields = ('dni',)
    list_filter = ('id',)
    date_hierarchy = 'creado'


# @admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_caja', 'estado', 'fecha_cierre', 'saldo_inicial', 'monto_cierre')

# @admin.register(Planilla)


class PlanillaAdmin(admin.ModelAdmin):
    list_display = ('id', 'planilla_caja', 'planilla_cobrador', 'fecha_emision',
                    'fecha_cierre', 'monto_total', 'estado', 'cantidad_recibos')
    search_fields = ('planilla_caja', 'planilla_cobrador')
    list_filter = ('estado',)
    date_hierarchy = 'fecha_emision'

# @admin.register(Comprobante)


class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'comprobante_cliente', 'fecha_comprobante',
                    'monto')
    search_fields = ('monto', 'comprobante_cliente')
    date_hierarchy = 'fecha_comprobante'

# @admin.register(ComprobanteGenerado)


class ComprobanteGeneradoAdmin(admin.ModelAdmin):
    list_display = ('id', 'comprobante_recibo', 'comprobante_generado', 'monto')
    search_fields = ('comprobante_generado',)
    list_filter = ('monto',)

# @admin.register(Recibo)


class ReciboAdmin(admin.ModelAdmin):
    list_display = ('id', 'recibo_planilla', 'recibo_caja', 'monto', 'fecha', 'estado',
                    'comprobantes', 'cheque')
    search_fields = ('monto',)
    list_filter = ('estado',)
    date_hierarchy = 'fecha'


class AnticipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'anticipo_recibo', 'anticipo_comprobante', 'monto')
    search_fields = ('anticipo_comprobante',)
    list_filter = ('monto',)

# @admin.register(Banco)


class BancoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('nombre',)
    list_filter = ('id',)

# @admin.register(Cheque)


class ChequeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cheque_banco', 'numero', 'monto', 'imagen')
    search_fields = ('numero',)
    list_filter = ('id', 'monto',)

    # def formfield_for_foreignkey(self, db_field, request, **kwards):
    #     if db_field_name == 'cheque_banco':
    #         kwargs['queryset'] = Banco.objects.__all__.order_by('nombre')
    #         return super(ChequeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # if db_field_name == 'cheque_recibo':
    #     kwargs['queryset'] = Recibo.objects.__all__


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
