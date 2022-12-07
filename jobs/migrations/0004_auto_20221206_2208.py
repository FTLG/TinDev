# Generated by Django 3.2.13 on 2022-12-06 22:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20221206_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 22, 8, 40, 537008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 22, 8, 40, 537036, tzinfo=utc)),
        ),
    ]