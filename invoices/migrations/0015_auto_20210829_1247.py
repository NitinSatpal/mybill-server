# Generated by Django 3.2 on 2021-08-29 12:47

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_auto_20210821_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Value to be used for buyer commission, It can be of any type based on commission type.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Buyer price for commission as per price_for_commission_applied_to.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Value to be used for discount, It can be of any type based on discount type.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Value to be used for seller commission, It can be of any type based on commission type.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Seller price for commission as per price_for_commission_applied_to.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Total price for this invoice.', max_digits=55, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]