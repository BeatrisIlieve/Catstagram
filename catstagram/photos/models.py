# photos/models.py
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from catstagram.cats.models import Cat
from catstagram.core.model_mixins import StrFromFieldsMixin
from catstagram.photos.validators import validate_file_less_than_5mb

CatstagramUserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'publication_date')

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATIONS_LENGTH = 30

    photo = models.ImageField(
        upload_to='cat_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    locations = models.CharField(
        max_length=MAX_LOCATIONS_LENGTH,
        null=True,
        blank=True,
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

    user = models.ForeignKey(
        CatstagramUserModel,
        on_delete=models.RESTRICT,
    )
