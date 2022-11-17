from django.db import models

# Create the post model with specified attributes

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
