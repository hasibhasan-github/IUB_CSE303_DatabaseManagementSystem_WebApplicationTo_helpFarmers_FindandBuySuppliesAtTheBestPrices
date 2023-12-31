# Generated by Django 4.2.7 on 2023-12-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProduct',
            fields=[
                ('prod_ID', models.BigAutoField(auto_created=True, default=10000, primary_key=True, serialize=False)),
                ('supp_ID', models.IntegerField()),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('prod_name', models.CharField(max_length=30)),
            ],
        ),
    ]
