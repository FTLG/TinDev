from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Candidate, Recruiter

# Create the index page view - display all posts
class IndexView(ListView):
    template_name = 'application/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Candidate.objects

# Create a view for each individual post with all info
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/view.html'