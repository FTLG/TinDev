from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..forms import CandidateSignUpForm, FavoritePost, FilterPostCandidate
from ..decorators import candidate_required
from ..models import User, UserPost, Offer
import datetime


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

@login_required
@candidate_required
def candidate_home(request):
    return render(request, "jobs/candidates/candidate_home.html")

@login_required
@candidate_required
def view_all_posts_candidates(request):

    form = FilterPostCandidate(request.POST or None)
    status = None
    city = None
    state = None
    keywords = [" "]

    if request.GET:

        if 'status' in request.GET and request.GET['status'] == "inactive":
            status = "inactive"
        elif 'status' in request.GET and request.GET['status'] == "active":
            status = "active"

        if 'state' in request.GET:
            state = request.GET["state"]
        if 'city' in request.GET:
            city = request.GET["city"]

        if 'keywords' in request.GET and request.GET['keywords'] != '':
            keywords = request.GET["keywords"].replace(" ", ",").split(',')

    
    allposts = UserPost.objects.all().order_by('-date_published')

    if status == "inactive":
        allposts = UserPost.objects.filter(status="Inactive")
    elif status == "active":
        allposts = UserPost.objects.filter(status="Active")

    if state:
        if city:
            allposts = UserPost.objects.filter(state=state).filter(city=city)
        else:
            allposts = UserPost.objects.filter(state=state)

    if city:
        allposts = UserPost.objects.filter(city=city)

    if keywords != [" "]:
        k = set(keywords)
        temp = []

        for word in k:
            temp1 = UserPost.objects.filter(description__icontains = word)
            temp2 = UserPost.objects.filter(preferred_skills__icontains = word)
            
            if temp1:
                temp.append(temp1)
            if temp2:
                temp.append(temp2)
        if temp:
            allposts = temp[0]
        else:
            allposts = temp

    context = {'allposts': allposts, 'form':form}
    
    return render(request, 'jobs/candidates/view_all_posts_candidates.html', context)

@login_required
@candidate_required
def view_all_posts_candidates_interest(request):

    allposts = UserPost.objects.filter(favorites = request.user)

    context = {'allposts': allposts}
    
    return render(request, 'jobs/candidates/view_all_interest_posts_candidates.html', context)

@login_required
@candidate_required
def post_detail_view_candidates(request, url=None):

    post = get_object_or_404(UserPost, url=url)
    context= {'post': post, 'user':request.user }
    
    return render(request, 'jobs/candidates/post_detail_view_candidates.html', context)

@login_required
@candidate_required
def favorite_post(request, url):

    post = UserPost.objects.get(url=url)
    post.save()

    post.favorites.add(request.user)
    post.save()

    context= {'post': post}

    return render(request, 'jobs/candidates/post_detail_view_candidates.html', context)

@login_required
@candidate_required
def remove_favorite(request, url):

    post = UserPost.objects.get(url=url)
    post.save()

    post.favorites.remove(request.user)
    post.save()

    context= {'post': post}

    return render(request, 'jobs/candidates/post_detail_view_candidates.html', context)

@login_required
@candidate_required
def view_offers(request):

    offers = Offer.objects.filter(user=request.user)
    date = datetime.datetime.now().date() 

    context= {'offers': offers, 'date':date}
    
    return render(request, 'jobs/candidates/view_all_offers.html', context)


    return

@login_required
@candidate_required
def offer_detail_view(request, url=None):

    offer = Offer.objects.get(url=url)
    post = offer.post

    context= {'post': post, 'user':request.user, 'offer':offer}

    return render(request, 'jobs/candidates/offer_detail_view.html', context)

@login_required
@candidate_required
def accept_offer(request, url=None):

    offer = Offer.objects.get(url=url)
    user = User.objects.get(id=request.user.id)
    post = offer.post

    offer.save()
    user.save()

    offer.rejected = False
    offer.accepted = True
    user.accepted = True

    offer.save()
    user.save()

    context= {'post': post, 'user':user, 'offer':offer}

    return render(request, 'jobs/candidates/offer_detail_view.html', context)

@login_required
@candidate_required
def reject_offer(request, url=None):

    offer = Offer.objects.get(url=url)
    user = User.objects.get(id=request.user.id)
    post = offer.post

    offer.save()
    user.save()

    offer.rejected = True
    offer.accepted = False
    user.accepted = False

    offer.save()
    user.save()

    context= {'post': post, 'user':user, 'offer':offer}


    return render(request, 'jobs/candidates/offer_detail_view.html', context)