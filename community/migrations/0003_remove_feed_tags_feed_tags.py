# Generated by Django 4.1.2 on 2022-11-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_feed_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='tags',
        ),
        migrations.AddField(
            model_name='feed',
            name='tags',
            field=models.ManyToManyField(blank=True, to='community.tag'),
        ),
    ]
