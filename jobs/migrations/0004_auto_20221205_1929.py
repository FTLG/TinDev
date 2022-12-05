# Generated by Django 3.2.13 on 2022-12-05 19:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20221205_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 19, 29, 52, 11133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='location',
            field=models.CharField(default='Ex: Cincinnati, OH', max_length=50),
        ),
    ]
