# Generated by Django 3.1.3 on 2021-09-25 21:39

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilesettings', '0004_profilesettings_set_commission_per_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilesettings',
            name='buyer_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Value to be used for buyer commission, It can be of any type based on commission type.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='profilesettings',
            name='buyer_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Buyer price for commission as per price_for_commission_applied_to.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='profilesettings',
            name='seller_commission_value',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Value to be used for seller commission, It can be of any type based on commission type.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='profilesettings',
            name='seller_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Seller price for commission as per price_for_commission_applied_to.', max_digits=55, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
