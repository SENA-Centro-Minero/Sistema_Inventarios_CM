# Generated by Django 4.1.1 on 2022-10-12 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_empresa_municipio_usuario_empresa_usuario_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=90, verbose_name='Nombre Departamento'),
        ),
    ]