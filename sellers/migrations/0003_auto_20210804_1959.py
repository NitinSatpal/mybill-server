# Generated by Django 3.2 on 2021-08-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('sellers', '0002_seller_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='city',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address'),
        ),
    ]