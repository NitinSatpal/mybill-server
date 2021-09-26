# Generated by Django 3.2 on 2021-08-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0015_auto_20210829_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number_of_units',
            field=models.PositiveIntegerField(help_text='Number of units sold/transferred for this invoice.'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quantity_per_unit',
            field=models.PositiveIntegerField(help_text='Number of Quintal/KGs per unit.'),
        ),
    ]
