from django.urls import include, path

from .views import jobs, candidates, recruiters

urlpatterns = [
    path('', jobs.home, name='home'),

    path('candidates/', include(([
        path('', candidates.candidate_home, name='candidate_home'),
    ], 'jobs'), namespace='candidates')),

    path('recruiters/', include(([
        path('', recruiters.recruiter_home, name='recruiter_home'),
    ], 'jobs'), namespace='recruiters')),
]
