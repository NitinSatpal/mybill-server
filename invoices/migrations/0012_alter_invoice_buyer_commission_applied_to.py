# Generated by Django 3.2 on 2021-08-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0011_alter_invoice_seller_commission_applied_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_commission_applied_to',
            field=models.IntegerField(blank=True, choices=[(1, 'Per Quintal'), (2, 'Per Kilogram'), (3, 'Per Pound'), (4, 'Per Ounce'), (5, 'Per Stone'), (6, 'Per Gallon'), (7, 'Per Litre'), (8, 'Per Unit')], default=1, help_text='Buyer commission applied to what type of unit (Per Quintal/Per Kg/Whole Unit).', null=True),
        ),
    ]