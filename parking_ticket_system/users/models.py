from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
import uuid  # for unique Employee IDs


class User(AbstractUser):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # unique ID

    employee_type = models.CharField(
        max_length=20,
        choices=(
            ("administrator", "Administrator"),
            ("worker", "Worker"),
            ("supervisor", "Supervisor"),
            ("manager", "Manager"),
        ),
        default="worker",
        null=True,
    )

    phone_number = models.CharField(max_length=15, unique=True)
