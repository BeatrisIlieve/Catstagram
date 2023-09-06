# Generated by Django 4.2.4 on 2023-09-04 12:01

import catstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_description_alter_photo_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='mediafiles/cat_photos/', validators=[catstagram.photos.validators.validate_file_less_than_5mb]),
        ),
    ]