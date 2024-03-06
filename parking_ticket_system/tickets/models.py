from decimal import Decimal
from django.db import models
import uuid  # for unique ticket IDs


class Ticket(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # unique ID

    vehicle_type = models.CharField(
        max_length=20,
        choices=(
            ("car", "Car"),
            ("bike", "Bike"),
            ("scooty", "Scooty"),
            ("truck", "Truck"),
            ("bus", "Bus"),
            ("van", "Van"),
            ("auto", "Auto"),
            ("cycle", "Cycle"),
            ("other", "Other"),
        ),
        default="car",
        null=True,
    )

    vehicle_license_plate = models.CharField(max_length=20, unique=True)

    phone_number = models.CharField(max_length=15, unique=True)

    entry_time = models.DateTimeField(auto_now_add=True)

    exit_time = models.DateTimeField(null=True, blank=True)

    parked_duration = models.DurationField(null=True, blank=True)

    amount_due = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )

    is_paid = models.BooleanField(
        default=False
    )  # Placeholder for future payment integration
