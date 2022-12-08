# Generated by Django 3.2.13 on 2022-12-07 19:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20221207_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 12, 7, 19, 30, 8, 684248, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 19, 30, 8, 682880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 7, 19, 30, 8, 682912, tzinfo=utc)),
        ),
    ]