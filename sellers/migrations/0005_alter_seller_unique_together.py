# Generated by Django 3.2 on 2021-09-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210804_1959'),
        ('sellers', '0004_seller_products'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seller',
            unique_together={('name', 'contact_phone_number', 'profile')},
        ),
    ]
