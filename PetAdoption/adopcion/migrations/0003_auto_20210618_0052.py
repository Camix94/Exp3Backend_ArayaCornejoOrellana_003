# Generated by Django 3.2.4 on 2021-06-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_auto_20210618_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fonoContacto',
            field=models.IntegerField(verbose_name='Telefono de Contacto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.CharField(max_length=500, verbose_name='Mensaje'),
        ),
    ]