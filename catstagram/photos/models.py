# photos/models.py
from django.core.validators import MinLengthValidator
from django.db import models

from catstagram.cats.models import Cat


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATIONS_LENGTH = 30

    photo = models.ImageField(
        null=False,
        blank=True,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    locations = models.CharField(
        max_length=MAX_LOCATIONS_LENGTH,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=False,
    )

    tagged_cats = models.ManyToManyField(
        Cat,
        blank=True,
    )
