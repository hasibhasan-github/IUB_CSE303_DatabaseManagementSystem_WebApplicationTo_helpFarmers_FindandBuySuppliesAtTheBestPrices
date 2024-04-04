# Generated by Django 4.2.7 on 2023-12-16 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Supplier', '0001_initial'),
        ('Farmer', '0002_remove_ftable_suppliertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='oTable',
            fields=[
                ('orderId', models.BigAutoField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('farmerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmer.ftable')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.ptable')),
                ('supplierID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Supplier.stable')),
            ],
        ),
    ]