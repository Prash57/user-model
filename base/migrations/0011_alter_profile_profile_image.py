# Generated by Django 3.2.11 on 2022-11-04 04:57

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20221104_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=base.models.profile_rename_upload),
        ),
    ]
