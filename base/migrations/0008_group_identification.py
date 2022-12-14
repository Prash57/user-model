# Generated by Django 4.1.2 on 2022-11-02 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_remove_profile_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('group', models.CharField(choices=[('Social', 'Social'), ('Professional', 'Professional'), ('Community', 'Community')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('aadhar', models.IntegerField(blank=True, null=True)),
                ('aadhar_image', models.ImageField(blank=True, default=None, null=True, upload_to='aadhar_images/')),
                ('tags', models.ManyToManyField(blank=True, to='base.tag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
