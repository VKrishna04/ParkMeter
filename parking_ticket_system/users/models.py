from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add custom user fields here if needed (e.g., employee ID)
    pass
