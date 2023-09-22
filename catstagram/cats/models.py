# cats/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from catstagram.core.model_mixins import StrFromFieldsMixin
from catstagram.photos.validators import validate_file_less_than_5mb

CatstagramUserModel = get_user_model()

class Cat(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')

    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.ImageField(
        upload_to='cat_photos/',
        null=False,
        blank=False,
        validators=(validate_file_less_than_5mb,),
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        CatstagramUserModel,
        on_delete=models.RESTRICT,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)