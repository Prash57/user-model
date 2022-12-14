# Generated by Django 3.2.11 on 2022-11-04 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_identification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identification',
            name='aadhar_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='aadhar_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile'),
        ),
    ]
