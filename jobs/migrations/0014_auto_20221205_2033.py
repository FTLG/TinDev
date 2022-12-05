# Generated by Django 3.2.13 on 2022-12-05 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20221205_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 20, 33, 19, 277611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 20, 33, 19, 277647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='job_type',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship')], default='Ex: Part Time', max_length=20),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50),
        ),
    ]
