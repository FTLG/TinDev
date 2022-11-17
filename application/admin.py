from django.contrib import admin
from .models import Candidate, Recruiter

# Register the post model

admin.site.register(Candidate)
admin.site.register(Recruiter)
