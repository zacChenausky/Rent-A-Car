# Generated by Django 4.0.6 on 2022-08-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_vehicle_body_alter_vehicle_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Vehicle Price'),
        ),
    ]
