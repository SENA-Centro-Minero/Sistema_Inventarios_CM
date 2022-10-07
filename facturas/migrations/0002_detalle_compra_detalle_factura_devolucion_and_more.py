# Generated by Django 4.1.1 on 2022-10-07 00:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_empresa_municipio_usuario_empresa_usuario_municipio'),
        ('productos', '0001_initial'),
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad')),
                ('precio', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad')),
                ('precio', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('lote', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Lote')),
                ('fechaExpiracion', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Expiración')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('codigoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Código Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDevolucion', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Devolución')),
                ('observaciones', models.TextField(max_length=200, verbose_name='Observaciones')),
                ('monto', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto')),
                ('detalleCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.detalle_compra', verbose_name='Detalle Compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.ManyToManyField(related_name='Cliente', to='usuarios.usuario', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='factura',
            name='empleado',
            field=models.ManyToManyField(related_name='Empleado', to='usuarios.usuario', verbose_name='Empleado'),
        ),
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='factura',
            name='monto',
            field=models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto'),
        ),
        migrations.AddField(
            model_name='factura',
            name='numeroSerie',
            field=models.TextField(default=0, max_length=80, verbose_name='Número de Serie'),
        ),
        migrations.AddField(
            model_name='factura',
            name='tipoFactura',
            field=models.CharField(choices=[('Venta', 'Venta'), ('Compra', 'Compra')], default='Venta', max_length=6, verbose_name='Tipo de Factura'),
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='numeroFactura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.factura', verbose_name='Número Factura'),
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='detalleFactura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.detalle_factura', verbose_name='Detalle Factura'),
        ),
        migrations.AddField(
            model_name='detalle_compra',
            name='numeroFactura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.factura', verbose_name='Número Factura'),
        ),
    ]
