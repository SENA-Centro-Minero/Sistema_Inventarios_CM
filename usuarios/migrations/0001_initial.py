# Generated by Django 4.1.1 on 2022-10-06 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=90, verbose_name='Nombre Departamento')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=80, verbose_name='Nombre Empresa')),
                ('nit', models.TextField(max_length=20, verbose_name='NIT Empresa')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=90, verbose_name='Nombre Municipio')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.departamento', verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('tipoDocumento', models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=4, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=50, verbose_name='Número de Documento')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=70, verbose_name='Dirección')),
                ('fecha_nacimiento', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Nacimiento')),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Empleado', 'Empleado'), ('Cliente', 'Cliente'), ('Proveedor', 'Proveedor')], default='Empleado', max_length=13, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.municipio', verbose_name='Municipio')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.sucursal', verbose_name='Sucursal')),
            ],
        ),
    ]
