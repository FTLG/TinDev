# Generated by Django 3.2.13 on 2022-12-06 21:27

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_candidate', models.BooleanField(default=False)),
                ('is_recruiter', models.BooleanField(default=False)),
                ('name', models.CharField(default='STRING', max_length=30)),
                ('zipcode', models.CharField(default='STRING', max_length=30)),
                ('bio', models.CharField(default='STRING', max_length=30)),
                ('github', models.CharField(default='STRING', max_length=30)),
                ('experience', models.CharField(default='STRING', max_length=30)),
                ('education', models.CharField(default='STRING', max_length=30)),
                ('company', models.CharField(default='STRING', max_length=30)),
                ('skills', models.CharField(default='STRING', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('job_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship')], default='Ex: Part Time', max_length=20)),
                ('state', models.CharField(default='Ex: Ohio', max_length=50)),
                ('city', models.CharField(default='Ex: Cincinnati', max_length=50)),
                ('preferred_skills', models.CharField(default='Ex: Python, Java', max_length=500)),
                ('description', models.CharField(default='Enter Description Here', max_length=500)),
                ('company', models.CharField(default='Company Name', max_length=50)),
                ('date_published', models.DateTimeField(default=datetime.datetime(2022, 12, 6, 21, 27, 44, 219991, tzinfo=utc))),
                ('expire_date', models.DateTimeField(default=datetime.datetime(2022, 12, 6, 21, 27, 44, 220018, tzinfo=utc))),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50)),
                ('url', models.SlugField(blank=True, editable=False, max_length=500, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('favorites', models.ManyToManyField(related_name='favorite_job', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_job', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
