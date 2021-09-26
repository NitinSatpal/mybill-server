# Generated by Django 3.2 on 2021-07-25 09:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the seller company.', max_length=32, verbose_name='name')),
                ('contact_first_name', models.CharField(help_text='First name of the seller company contact person.', max_length=32, verbose_name='name')),
                ('contact_last_name', models.CharField(help_text='Last name of the seller company contact person.', max_length=32, verbose_name='name')),
                ('contact_email', models.EmailField(blank=True, help_text='Email of the seller company contact person.', max_length=64, null=True, verbose_name='contact email')),
                ('contact_phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number of the seller company contact person.', max_length=128, region=None, verbose_name='phone number')),
                ('address_line_1', models.CharField(blank=True, default='', help_text='Address line one of the seller company.', max_length=128, verbose_name='address line 1')),
                ('address_line_2', models.CharField(blank=True, default='', help_text='Address line two of the seller company.', max_length=128, verbose_name='address line 2')),
                ('postal_code', models.IntegerField(blank=True, default=None, help_text='Postal code of the seller company.', null=True, verbose_name='postal code')),
                ('city', models.CharField(blank=True, default='', help_text='City of the seller company.', max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'verbose_name': 'Buyer',
                'verbose_name_plural': 'Buyers',
                'unique_together': {('name', 'contact_phone_number')},
            },
        ),
    ]
