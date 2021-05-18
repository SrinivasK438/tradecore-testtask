from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username = None

    email = models.EmailField(
        unique=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    country = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    country_code = models.CharField(
        max_length=5,
        null=True,
        blank=True,
    )

    country_geoname_id = models.IntegerField(
        null=True,
        blank=True,
    )

    longitude = models.FloatField(
        null=True,
        blank=True,
    )

    latitude = models.FloatField(
        null=True,
        blank=True,
    )

    joined_on_holiday = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
