# Generated by Django 3.0.7 on 2020-09-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGCapp', '0002_auto_20200905_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheque',
            name='cheque_recibo',
        ),
    ]