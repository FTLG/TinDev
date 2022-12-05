# Generated by Django 3.2.13 on 2022-12-05 19:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20221205_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='content',
        ),
        migrations.AddField(
            model_name='userpost',
            name='job_type',
            field=models.CharField(default='Ex: Part Time', max_length=500),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 19, 31, 36, 527267, tzinfo=utc)),
        ),
    ]
