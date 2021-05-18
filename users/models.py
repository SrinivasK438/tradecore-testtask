from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ip_address = models.GenericIPAddressField()

    country = models.CharField(
        max_length=50,
    )

    country_code = models.CharField(
        max_length=5,
    )

    country_geoname_id = models.IntegerField()

    longitude = models.FloatField()

    latitude = models.FloatField()

    joined_on_holiday = models.BooleanField(
        default=False,
    )
