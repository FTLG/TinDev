# Generated by Django 3.2.13 on 2022-12-05 19:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20221205_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='company',
            field=models.CharField(default='Company Name', max_length=50),
        ),
        migrations.AddField(
            model_name='userpost',
            name='description',
            field=models.CharField(default='Enter Description Here', max_length=500),
        ),
        migrations.AddField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 19, 45, 27, 211349, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 19, 45, 27, 211323, tzinfo=utc)),
        ),
    ]