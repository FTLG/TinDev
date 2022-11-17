from django.db import models

# Create the post model with specified attributes

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    profile_bio = models.TextField()
    zipcode = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    years_exp = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Recruiter(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)