# Generated by Django 3.0.7 on 2020-09-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGCapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheque',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cheque/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='cheque',
            name='cheque_recibo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGCapp.Recibo', verbose_name='Recibo'),
        ),
    ]