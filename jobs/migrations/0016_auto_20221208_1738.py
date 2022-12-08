# Generated by Django 3.2.13 on 2022-12-08 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20221208_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 17, 38, 8, 8343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.CharField(default='STRING', max_length=5),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 17, 38, 8, 7004, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 17, 38, 8, 7030, tzinfo=utc)),
        ),
    ]
