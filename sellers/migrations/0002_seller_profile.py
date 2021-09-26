# Generated by Django 3.2 on 2021-08-03 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_unique_together'),
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]