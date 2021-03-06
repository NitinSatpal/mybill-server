# Generated by Django 3.2 on 2021-08-28 04:11

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the seller company.', max_length=32, unique=True, verbose_name='name')),
                ('minimum_quantity', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Minimum quantity of the product that must be ordered or bought.', max_digits=55, null=True)),
                ('quantity_measurement_unit', models.IntegerField(choices=[(1, 'Quintal'), (2, 'Kilogram'), (3, 'Pound'), (4, 'Ounce'), (5, 'Stone'), (6, 'Gallon'), (7, 'Litre')], default=1, help_text='Measure unit of a unit like Quintal/Kgs.')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
