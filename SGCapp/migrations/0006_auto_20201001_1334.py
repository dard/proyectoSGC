# Generated by Django 3.0.7 on 2020-10-01 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGCapp', '0005_auto_20200925_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibo',
            name='medios_de_pago',
        ),
        migrations.AddField(
            model_name='recibo',
            name='cheque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cheque', verbose_name='Nro Cheque'),
        ),
        migrations.AlterField(
            model_name='anticipo',
            name='anticipo_comprobante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Comprobante', verbose_name='Nro_Comprobante'),
        ),
        migrations.AlterField(
            model_name='anticipo',
            name='anticipo_recibo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Recibo', verbose_name='Nro_Recibo'),
        ),
        migrations.AlterField(
            model_name='comprobantegenerado',
            name='comprobante_generado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Comprobante', verbose_name='Nro_Comprobante'),
        ),
        migrations.AlterField(
            model_name='comprobantegenerado',
            name='comprobante_recibo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Recibo', verbose_name='Nro_Recibo'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='fecha_emision',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha emision'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='planilla_caja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Caja', verbose_name='Caja id'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='planilla_cobrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cobrador', verbose_name='Cobrador id'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='recibo_caja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Caja', verbose_name='Nro Caja'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='recibo_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Cliente', verbose_name='Cliente DNI'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='recibo_planilla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Planilla', verbose_name='Nro Planilla'),
        ),
    ]