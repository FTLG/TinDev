from django.shortcuts import redirect, render
from django.views.generic import TemplateView

# Class for signing up
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

# Function to send user to appropriate home screen if they are logged in correctly
def home(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter:
            return redirect('recruiters:recruiter_home')
        else:
            return redirect('candidates:candidate_home')
    return render(request, 'jobs/home.html')
