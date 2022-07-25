# Generated by Django 4.0.6 on 2022-07-24 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_date', models.DateField(verbose_name='Out Date')),
                ('in_date', models.DateField(verbose_name='In Date')),
                ('confirmation_number', models.IntegerField(verbose_name='conf')),
                ('rented_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.vehicle')),
                ('renter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
