# Generated by Django 4.2.5 on 2023-09-22 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cats', '0005_alter_cat_personal_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
