# Generated by Django 3.2.4 on 2021-06-22 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0008_alter_mensajecontacto_fonocontacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajecontacto',
            name='id',
        ),
        migrations.AddField(
            model_name='mensajecontacto',
            name='rut',
            field=models.IntegerField(default=123, primary_key=True, serialize=False, verbose_name='Rut'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='correoContacto',
            field=models.EmailField(max_length=100, verbose_name='Correo de Contacto'),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='fonoContacto',
            field=models.IntegerField(verbose_name='Telefono de Contacto'),
        ),
    ]
