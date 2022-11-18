from django.urls import include, path

from jobs.views import jobs, candidates, recruiters

urlpatterns = [
    path('', include('jobs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', jobs.SignUpView.as_view(), name='signup'),
    path('accounts/signup/candidate/', candidates.CandidateSignUpView.as_view(), name='candidate_signup'),
    path('accounts/signup/recruiter/', recruiters.RecruiterSignUpView.as_view(), name='recruiter_signup'),
]
