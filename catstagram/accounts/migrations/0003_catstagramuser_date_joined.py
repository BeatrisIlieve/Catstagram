# Generated by Django 4.2.5 on 2023-09-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catstagramuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-01'),
            preserve_default=False,
        ),
    ]