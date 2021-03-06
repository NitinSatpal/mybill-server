# Generated by Django 3.2 on 2021-08-15 10:11

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_auto_20210815_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='commission_applied_to',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='commission_type',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='commission_value',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price_for_commission',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price_for_commission_applied_to',
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_commission_applied_to',
            field=models.IntegerField(choices=[(1, 'Per Quintal'), (2, 'Per Kilogram'), (3, 'Per Pound'), (4, 'Per Ounce'), (5, 'Per Stone'), (6, 'Per Gallon'), (7, 'Per Litre'), (8, 'Per Unit')], default=1, help_text='Buyer commission applied to what type of unit (Per Quintal/Per Kg/Whole Unit).'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_commission_type',
            field=models.IntegerField(choices=[(1, 'Fixed'), (2, 'Percent')], default=1, help_text='Is buyer commission fixed or in per cent.'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_commission_value',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Value to be used for buyer commission, It can be of any type based on commission type.', max_digits=55),
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Buyer price for commission as per price_for_commission_applied_to.', max_digits=55, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='buyer_price_for_commission_applied_to',
            field=models.IntegerField(choices=[(1, 'Per Quintal'), (2, 'Per Kilogram'), (3, 'Per Pound'), (4, 'Per Ounce'), (5, 'Per Stone'), (6, 'Per Gallon'), (7, 'Per Litre'), (8, 'Per Unit')], default=8, help_text='Buyer price used for commission calculations, applied to what type of unit (Per Quintal/Per Kg/Whole Unit).'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='only_buyer_commission',
            field=models.BooleanField(default=False, help_text='Deduct commission only from buyer.'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='only_seller_commission',
            field=models.BooleanField(default=False, help_text='Deduct commission only from seller.'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller_commission_applied_to',
            field=models.IntegerField(choices=[(1, 'Per Quintal'), (2, 'Per Kilogram'), (3, 'Per Pound'), (4, 'Per Ounce'), (5, 'Per Stone'), (6, 'Per Gallon'), (7, 'Per Litre'), (8, 'Per Unit')], default=1, help_text='Seller commission applied to what type of unit (Per Quintal/Per Kg/Whole Unit).'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller_commission_type',
            field=models.IntegerField(choices=[(1, 'Fixed'), (2, 'Percent')], default=1, help_text='Is seller commission fixed or in per cent.'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller_commission_value',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='Value to be used for seller commission, It can be of any type based on commission type.', max_digits=55),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller_price_for_commission',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), help_text='Seller price for commission as per price_for_commission_applied_to.', max_digits=55, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller_price_for_commission_applied_to',
            field=models.IntegerField(choices=[(1, 'Per Quintal'), (2, 'Per Kilogram'), (3, 'Per Pound'), (4, 'Per Ounce'), (5, 'Per Stone'), (6, 'Per Gallon'), (7, 'Per Litre'), (8, 'Per Unit')], default=8, help_text='Seller price used for commission calculations, applied to what type of unit (Per Quintal/Per Kg/Whole Unit).'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='separate_commission_for_seller_and_buyer',
            field=models.BooleanField(default=False, help_text='Deduct diffrent commissions from seller and buyer.'),
        ),
    ]
