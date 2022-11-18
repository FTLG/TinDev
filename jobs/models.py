from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


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

