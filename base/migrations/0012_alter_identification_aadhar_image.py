# Generated by Django 3.2.11 on 2022-11-04 04:58

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identification',
            name='aadhar_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=base.models.aadhar_rename_upload),
        ),
    ]
