# Generated by Django 4.1.1 on 2022-10-07 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_usuario_municipio_remove_usuario_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarioMunicipio', to='usuarios.municipio', verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.empresa', verbose_name='Empresa'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.municipio', verbose_name='Municipio'),
        ),
    ]
