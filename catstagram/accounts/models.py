from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from catstagram.core.model_mixins import ChoicesEnumMixin
from catstagram.core.validators import validate_only_letters
from catstagram.photos.validators import validate_file_less_than_5mb


class Gender(ChoicesEnumMixin, Enum):
    Female = 'Female'
    Male = 'Male'
    DoNotShow = 'Do not Show'


class CatstagramUser(AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(
                FIRST_NAME_MIN_LENGTH,
            ),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(
                LAST_NAME_MIN_LENGTH,
            ),
            validate_only_letters,
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),
    )

    personal_photo = models.ImageField(
        upload_to='account_photos/',
        null=False,
        blank=False,
        validators=(validate_file_less_than_5mb,),
    )
