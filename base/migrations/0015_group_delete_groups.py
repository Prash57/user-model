# Generated by Django 4.1.2 on 2022-11-08 07:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_rename_group_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(choices=[('Social', 'Social'), ('Professional', 'Professional'), ('Community', 'Community')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]