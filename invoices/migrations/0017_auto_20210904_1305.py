# Generated by Django 3.2 on 2021-09-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0016_auto_20210829_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='partial_paid',
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'Paid'), (2, 'Unpaid'), (3, 'Partial Paid')], default=2, help_text='Is this invoice paid, unpaid or partially paid.'),
        ),
    ]