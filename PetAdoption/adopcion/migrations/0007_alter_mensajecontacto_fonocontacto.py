# Generated by Django 3.2.4 on 2021-06-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0006_mensajecontacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajecontacto',
            name='fonoContacto',
            field=models.CharField(max_length=12, verbose_name='Telefono de Contacto'),
        ),
    ]
