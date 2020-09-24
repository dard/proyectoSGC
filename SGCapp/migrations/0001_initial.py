# Generated by Django 3.0.7 on 2020-09-24 12:57

import builtins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('A', 'Abierta'), ('C', 'Cerrada')], max_length=1)),
                ('fecha_cierre', models.DateTimeField(auto_now=True, verbose_name='fecha cierre')),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='saldo inicial')),
                ('monto_cierre', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='monto cierre')),
                ('user_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_caja', to=settings.AUTH_USER_MODEL, verbose_name='usuario caja')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=25, null=True, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('direccion', models.CharField(blank=True, max_length=40, null=True, verbose_name='Dirección')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cobrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=25, null=True, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
                ('telefono', models.IntegerField(null=True, verbose_name='Telefono')),
                ('direccion', models.CharField(blank=True, max_length=40, null=True, verbose_name='Dirección')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cobrador',
                'verbose_name_plural': 'Cobradores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_comprobante', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('monto_original', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto')),
                ('monto_cancelado', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto Cancelado')),
                ('comprobante_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cliente', verbose_name='Cliente')),
            ],
            options={
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True, verbose_name='fecha emision')),
                ('fecha_cierre', models.DateTimeField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto Total')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado')),
                ('cantidad_recibos', models.IntegerField(verbose_name='Cantidad de Recibos')),
                ('planilla_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Caja', verbose_name='caja')),
                ('planilla_cobrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cobrador', verbose_name='cobrador')),
            ],
            options={
                'verbose_name': 'Planilla',
                'verbose_name_plural': 'Planillas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado')),
                ('comprobantes_Cancelados', models.CharField(max_length=10, verbose_name='Comprobantes Cancelados')),
                ('monto_comprobantes', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto Comprobantes')),
                ('medios_de_pago', models.CharField(max_length=10, verbose_name='Medios de Pago')),
                ('recibo_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Caja', verbose_name='Caja')),
                ('recibo_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cliente', verbose_name='Cliente')),
                ('recibo_planilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Planilla', verbose_name='Planilla')),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ComprobanteGenerado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto')),
                ('comprobante_generado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Comprobante', verbose_name='Comprobante')),
                ('comprobante_recibo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Recibo', verbose_name='Recibo')),
            ],
            options={
                'ordering': [builtins.id],
            },
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.DecimalField(decimal_places=0, max_digits=10, unique=True, verbose_name='Numero Cheque')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Monto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cheque/%Y/%m/%d')),
                ('cheque_banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Banco', verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Cheque',
                'verbose_name_plural': 'Cheques',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Anticipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Monto')),
                ('anticipo_comprobante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Comprobante', verbose_name='Comprobante')),
                ('anticipo_recibo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Recibo', verbose_name='Recibo')),
            ],
            options={
                'verbose_name': 'Anticipo',
                'verbose_name_plural': 'Anticipos',
                'ordering': [builtins.id],
            },
        ),
    ]
