# Generated by Django 4.2.7 on 2024-02-23 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_channel_name_channel_channel_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 23, 19, 55, 26, 412912, tzinfo=datetime.timezone.utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]