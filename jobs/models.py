from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import TextInput
from django.core.validators import RegexValidator

import datetime
import uuid
import string

# Define types of jobs
POSITION_TYPE = [('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Internship', 'Internship')]

# Define job status
STATUS = [('Active', 'Active'), ('Inactive', 'Inactive')]

# Create user model
class User(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    name = models.CharField(max_length=30, default="STRING")
    zipcode = models.IntegerField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    bio = models.CharField(max_length=30, default="STRING")
    github = models.CharField(max_length=30, default="STRING")
    experience = models.CharField(max_length=30, default="STRING")
    education = models.CharField(max_length=30, default="STRING")
    company = models.CharField(max_length=30, default="STRING")
    skills = models.CharField(max_length=30, default="STRING")
    accepted = models.BooleanField(default=False)


# Create model for User's Jobs
class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_job')
    title = models.CharField(max_length=500)
    job_type = models.CharField(max_length=20, choices=POSITION_TYPE, blank=False)
    state = models.CharField(max_length = 50, blank=False)
    city = models.CharField(max_length = 50, blank=False)
    preferred_skills = models.CharField(max_length = 500, blank=False)
    description = models.CharField(max_length = 500, blank=False)
    company = models.CharField(max_length = 50, blank=False)
    date_published = models.DateTimeField(default=timezone.now())
    expire_date = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length = 50, choices=STATUS, blank=False)
    url = models.SlugField(max_length=500, unique=True, blank=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    favorites = models.ManyToManyField(User, related_name='favorite_job')

    def save(self, *args, **kwargs):
        self.url= slugify(self.id)
        super(UserPost, self).save(*args, **kwargs)

    # Function to sort match the most qualified candidates to the job based on mostly skills, but also bio and job description
    def favorites_ranked(self):
        list_interested = []
        for user in self.favorites.all():
          
            # Calculate common words in bios  
            description_simple = self.description.lower().translate(str.maketrans('', '', string.punctuation))
            bio_simple = user.bio.lower().translate(str.maketrans('', '', string.punctuation))
            description_list = description_simple.split(" ")
            bio_list = bio_simple.split(" ")
            num_common_bios = len(list(set(description_list)&set(bio_list)))

            # Calculate common skills
            pref_skills_simple = self.preferred_skills.lower().translate(str.maketrans('', '', string.punctuation))
            user_skills_simple = user.skills.lower().translate(str.maketrans('', '', string.punctuation))
            pref_skills_list = pref_skills_simple.split(" ")
            user_skills_list = user_skills_simple.split(" ")
            num_common_skills = len(list(set(pref_skills_list)&set(user_skills_list)))

            # Weight skills more heavily than bio
            user.compat = int(40 * num_common_bios / len(description_list) + 60 * num_common_skills / len(pref_skills_list))

            list_interested.append(user)
        
        cands_sorted = sorted(list_interested, key=lambda x: x.compat, reverse=True)
        
        return cands_sorted


# Model to make an job offer
class Offer(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='offer_user')
    post = models.ForeignKey(UserPost, on_delete=models.PROTECT, related_name='offer_post')
    salary = models.CharField(max_length=25)
    deadline = models.DateField(default=timezone.now())
    url = models.SlugField(max_length=500, unique=True, blank=True, editable=False)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def save(self, *args, **kwargs):
        self.url= slugify(self.id)
        super(Offer, self).save(*args, **kwargs)
