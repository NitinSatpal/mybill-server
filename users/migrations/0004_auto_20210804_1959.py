# Generated by Django 3.2 on 2021-08-04 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.IntegerField(choices=[(1, 'Personal'), (2, 'Business')], default=2),
        ),
    ]
