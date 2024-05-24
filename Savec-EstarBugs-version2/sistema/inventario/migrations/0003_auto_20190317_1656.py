

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20190317_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_negocio', models.CharField(max_length=25, null=True)),
                ('mensaje', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Opciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneda', models.CharField(max_length=5, null=True)),
                ('valor_iva', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('sub_monto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('monto_general', models.DecimalField(decimal_places=2, max_digits=9)),
                ('iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Opciones', to_field='valor_iva')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
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
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Cliente', to_field='cedula'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Opciones', to_field='valor_iva'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='disponible',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Proveedor', to_field='cedula'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='id_pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Pedido'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto'),
        ),
    ]
