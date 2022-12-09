from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from ..decorators import recruiter_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from ..decorators import recruiter_required
from ..forms import RecruiterSignUpForm, UserPostForm, InterestedCandidatesForm, FilterPost
from ..models import User, UserPost, Offer
import logging

# Class to sign up a recruiter
class RecruiterSignUpView(CreateView):
    model = User
    form_class = RecruiterSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'recruiter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('recruiters:recruiter_home')

# Function to render recruiter home screen

@login_required
@recruiter_required
def recruiter_home(request):
    return render(request, "jobs/recruiters/recruiter_home.html")

# Function to create job posting

@login_required
@recruiter_required
def create_post(request):
    form = UserPostForm(request.POST or None)
    user = request.user

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
        return redirect("recruiters:view_all_posts")

    context= {'form': form}

    return render(request, 'jobs/recruiters/create_post.html', context)

# Function for recruiter to view the jobs they have posted

@login_required
@recruiter_required
def view_all_posts(request):

    form = FilterPost(request.POST or None)
    reset_search = False
    status = None
    one_interested = False

    if request.GET:

        if 'reset_search' in request.GET and request.GET['reset_search'] == "on":
            reset_search = True

        # Set status
        if 'status' in request.GET and request.GET['status'] == "inactive":
            status = "inactive"
        elif 'status' in request.GET and request.GET['status'] == "active":
            status = "active"

        # Set whether interested
        if 'at_least_one_interested' in request.GET and request.GET['at_least_one_interested'] == "on":
            one_interested = True

    # Order by date published
    allposts = UserPost.objects.filter(user=request.user).order_by('-date_published')

    # Filter by status
    if status == "inactive":
        allposts = UserPost.objects.filter(user=request.user).filter(status="Inactive")
    elif status == "active":
        allposts = UserPost.objects.filter(user=request.user).filter(status="Active")

    # Filter by whether interested
    if one_interested:
        allposts = UserPost.objects.filter(user=request.user).annotate(c=Count('favorites')).filter(c__gt=0)

    # Reset search if needed
    if reset_search:
        allposts = UserPost.objects.filter(user=request.user).order_by('-date_published')
    
    context = {'allposts': allposts, 'form':form}
    
    return render(request, 'jobs/recruiters/view_all_posts.html', context)

# Function to display detailed view of post as recruiter

@login_required
@recruiter_required
def post_detail_view(request, url=None):

    post= get_object_or_404(UserPost, url=url)
    context= {'post': post, 'offered':[]}
    
    return render(request, 'jobs/recruiters/post_detail_view.html', context)

# Function to edit post

@login_required
@recruiter_required
def edit_post(request, url):
    post = UserPost.objects.get(url=url)
    form = UserPostForm(request.POST or None, instance=post)

    user = request.user

    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.title = request.POST.get('title')
            post.save()
        return redirect("recruiters:view_all_posts")
    
    context= {'form': form}

    return render(request, 'jobs/recruiters/create_post.html', context)

@login_required
@recruiter_required
def delete_post(request, url):

    UserPost.objects.filter(url=url).delete()

    return redirect('recruiters:view_all_posts')

# Function to view candidates that are interested in a post
@login_required
@recruiter_required
def view_interested(request, url):

    post = UserPost.objects.get(url=url)
    users = post.favorites_ranked()
    # save choices as a tuple to pass into the form 
    choices = [(x, (x.name + "  - Compatability Score: " + str(x.compat) +"%")) for x in users]

    # get all current offers
    current_offers = Offer.objects.all()

    # if a user already has an offer for that post, don't include them
    for curr in current_offers:
        for curr_user, string in choices:
            if curr.post == post and curr.user == curr_user:
                temp_user = User.objects.filter(username=curr_user)[0]
                choices.remove((temp_user, string))

    form = InterestedCandidatesForm(request.POST or None, choices=choices)

    # on form submission, save the offer to db
    if request.method == "POST":
        if form.is_valid():

            offer_salary = request.POST.get('salary')
            offer_deadline = request.POST.get('deadline')
            selected_candidates = form.cleaned_data['interested_candidates']

            for candidate in selected_candidates:

                offer_user = User.objects.filter(username=candidate)[0]
                offer = Offer.objects.create(user=offer_user, post=post, salary=offer_salary, deadline=offer_deadline)
                offer.save()

            return redirect("recruiters:post_detail_view", url=url)

    
    offers = Offer.objects.all()

    context = {'post': post, 'users': users, 'form': form, 'offers':offers}

    return render(request, 'jobs/recruiters/view_interested.html', context)
