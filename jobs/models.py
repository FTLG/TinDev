from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.admin.widgets import AdminDateWidget
import datetime
import uuid

POSITION_TYPE = [('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship')]
STATUS = [('Active', 'Active'), ('Inactive', 'Inactive')]

class User(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    name = models.CharField(max_length=30, default="STRING")
    zipcode = models.CharField(max_length=30, default="STRING")
    bio = models.CharField(max_length=30, default="STRING")
    github = models.CharField(max_length=30, default="STRING")
    experience = models.CharField(max_length=30, default="STRING")
    education = models.CharField(max_length=30, default="STRING")
    company = models.CharField(max_length=30, default="STRING")
    skills = models.CharField(max_length=30, default="STRING")

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_job')
    title = models.CharField(max_length=500)
    job_type = models.CharField(max_length=20, choices=POSITION_TYPE, default="Ex: Part Time")
    state = models.CharField(max_length = 50, default="Ex: Ohio")
    city = models.CharField(max_length = 50, default="Ex: Cincinnati")
    preferred_skills = models.CharField(max_length = 500, default="Ex: Python, Java")
    description = models.CharField(max_length = 500, default="Enter Description Here")
    company = models.CharField(max_length = 50, default="Company Name")
    date_published = models.DateTimeField(default=timezone.now())
    expire_date = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length = 50, choices=STATUS, default="Active")
    url = models.SlugField(max_length=500, unique=True, blank=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    favorites = models.ManyToManyField(User, related_name='favorite_job')


    def save(self, *args, **kwargs):
        self.url= slugify(self.id)
        super(UserPost, self).save(*args, **kwargs)    
