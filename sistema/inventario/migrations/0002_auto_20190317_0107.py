
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=200)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('telefono2', models.CharField(max_length=20, null=True)),
                ('correo', models.CharField(max_length=20)),
                ('correo2', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('sub_monto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('monto_general', models.DecimalField(decimal_places=2, max_digits=9)),
                ('iva', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('disponible', models.IntegerField(default=0)),
                ('categoria', models.CharField(max_length=20, choices=[('1', 'Unidad'), ('2', 'Kilo'), ('3', 'Litro'), ('4', 'Otros')])),
                ('tiene_iva', models.BooleanField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='id_factura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Factura'),
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto'),
        ),
    ]
