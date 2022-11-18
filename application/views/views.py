from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Candidate, Recruiter


def index(request):
    return render(request, "application/index.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

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