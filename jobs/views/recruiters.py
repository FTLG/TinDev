from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from ..decorators import recruiter_required
from ..forms import RecruiterSignUpForm, UserPostForm
from ..models import User, UserPost


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


def recruiter_home(request):
    return render(request, "jobs/recruiters/recruiter_home.html")

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

def view_all_posts(request):

    allposts= UserPost.objects.filter(user=request.user).order_by('-date_published')
    context= {'allposts': allposts}
    
    return render(request, 'jobs/recruiters/view_all_posts.html', context)

def post_detail_view(request, url=None):

    post= get_object_or_404(UserPost, url=url)
    context= {'post': post}
    
    return render(request, 'jobs/recruiters/post_detail_view.html', context)

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

def delete_post(request, url):

    UserPost.objects.filter(url=url).delete()

    return redirect('recruiters:view_all_posts')

def view_interested(request, url):

    post = UserPost.objects.get(url=url)
    users = post.favorites.all()

    context = {'post': post, 'users': users}

    return render(request, 'jobs/recruiters/view_interested.html', context)
