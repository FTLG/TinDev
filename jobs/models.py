from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from django.utils.text import slugify
import datetime

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
    user= models.ForeignKey(User, on_delete=models.PROTECT)
    title= models.CharField(max_length=500)
    content= models.TextField()
    date_published= models.DateTimeField(default=timezone.now())
    url= models.SlugField(max_length=500, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(UserPost, self).save(*args, **kwargs)    
