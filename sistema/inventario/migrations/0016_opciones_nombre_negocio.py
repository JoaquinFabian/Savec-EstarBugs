# Generated by Django 5.0.4 on 2024-05-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_remove_opciones_nombre_negocio_alter_cliente_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opciones',
            name='nombre_negocio',
            field=models.CharField(default='EstarBugs', max_length=50),
        ),
    ]
