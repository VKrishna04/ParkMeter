# Generated by Django 5.0.3 on 2024-03-06 18:17

import uuid
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('bike', 'Bike'), ('scooty', 'Scooty'), ('truck', 'Truck'), ('bus', 'Bus'), ('van', 'Van'), ('auto', 'Auto'), ('cycle', 'Cycle'), ('other', 'Other')], default='car', max_length=20, null=True)),
                ('vehicle_license_plate', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField(blank=True, null=True)),
                ('parked_duration', models.DurationField(blank=True, null=True)),
                ('amount_due', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
    ]