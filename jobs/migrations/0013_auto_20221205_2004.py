# Generated by Django 3.2.13 on 2022-12-05 20:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20221205_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 20, 4, 38, 269179, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 20, 4, 38, 269222, tzinfo=utc)),
        ),
    ]