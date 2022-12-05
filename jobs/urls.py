from django.urls import include, path

from .views import jobs, candidates, recruiters

urlpatterns = [
    path('', jobs.home, name='home'),

    path('candidates/', include(([
        path('', candidates.candidate_home, name='candidate_home'),
    ], 'jobs'), namespace='candidates')),

    path('recruiters/', include(([
        path('', recruiters.recruiter_home, name='recruiter_home'),
        path('create/', recruiters.create_post, name='create_post'),
        path('posts/', recruiters.view_all_posts, name='view_all_posts'),
        path('posts/<slug:url>/', recruiters.post_detail_view, name='post_detail_view'),
    ], 'jobs'), namespace='recruiters')),
    
]
