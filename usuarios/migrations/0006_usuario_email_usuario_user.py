# Generated by Django 4.1.1 on 2022-10-27 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0005_usuario_foto_alter_departamento_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='a@b', max_length=150, verbose_name='Correo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
