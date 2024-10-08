# Generated by Django 5.1.1 on 2024-10-02 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightNumber', models.CharField(max_length=20)),
                ('airline', models.CharField(max_length=50)),
                ('departureCity', models.CharField(max_length=20)),
                ('arrivalCity', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight', to='flightApp.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to='flightApp.passenger')),
            ],
        ),
    ]
