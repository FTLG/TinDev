# Generated by Django 3.2.13 on 2022-12-08 02:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20221207_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 2, 54, 26, 530044, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 2, 54, 26, 528651, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 2, 54, 26, 528682, tzinfo=utc)),
        ),
    ]
