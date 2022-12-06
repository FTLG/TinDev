from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import CandidateSignUpForm
from ..decorators import candidate_required
from ..models import User, UserPost


class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('candidates:candidate_home')

def candidate_home(request):
    return render(request, "jobs/candidates/candidate_home.html")


def view_all_posts_candidates(request):

    allposts= UserPost.objects.all().order_by('-date_published')
    context= {'allposts': allposts}
    
    return render(request, 'jobs/candidates/view_all_posts_candidates.html', context)

def post_detail_view_candidates(request, url=None):

    post= get_object_or_404(UserPost, url=url)
    context= {'post': post}
    
    return render(request, 'jobs/candidates/post_detail_view_candidates.html', context)