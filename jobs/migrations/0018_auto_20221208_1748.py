# Generated by Django 3.2.13 on 2022-12-08 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20221208_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 17, 48, 38, 79461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 17, 48, 38, 78056, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 17, 48, 38, 78086, tzinfo=utc)),
        ),
    ]