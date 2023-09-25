from enum import Enum

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.db import models

from catstagram.accounts.manager import CatstagramUserManager
from catstagram.core.model_mixins import ChoicesEnumMixin
from catstagram.core.validators import validate_only_letters


# class Gender(ChoicesEnumMixin, Enum):
#     Female = 'Female'
#     Male = 'Male'
#     DoNotShow = 'Do not Show'


class CatstagramUser(AbstractBaseUser, PermissionsMixin,):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    # date_joined = models.DateTimeField(
    #     auto_now_add=True,
    # )

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    objects = CatstagramUserManager()





class Profile(models.Model):
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

    user = models.OneToOneField(
        CatstagramUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    # gender = models.CharField(
    #     choices=Gender.choices(),
    #     max_length=Gender.max_length(),
    # )
