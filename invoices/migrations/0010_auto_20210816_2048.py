# Generated by Django 3.2 on 2021-08-16 20:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_auto_20210815_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Value to be used for buyer commission, It can be of any type based on commission type.', max_digits=55, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Value to be used for seller commission, It can be of any type based on commission type.', max_digits=55, null=True),
        ),
    ]
