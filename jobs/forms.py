from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import DateInput
from jobs.models import (User, UserPost)



class RecruiterSignUpForm(UserCreationForm):
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    company = forms.CharField(label='Your Company', max_length=100, required=True)
    zipcode = forms.CharField(label='Your Zipcode', max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True
        user.company = self.cleaned_data["company"]
        user.name = self.cleaned_data["name"]
        user.zipcode = self.cleaned_data["zipcode"]

        if commit:
            user.save()
        return user


class CandidateSignUpForm(UserCreationForm):
    
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    zipcode = forms.CharField(label='Your Zipcode', max_length=100, required=True)
    github = forms.CharField(label='Your Github', max_length=100, required=False)
    bio = forms.CharField(label='Your Bio', max_length=100, required=False)
    skills = forms.CharField(label='Your Skills', max_length=100, required=True)
    experience = forms.CharField(label='Your Experience', max_length=100, required=True)
    education = forms.CharField(label='Your Education', max_length=100, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        user.name = self.cleaned_data["name"]
        user.zipcode = self.cleaned_data["zipcode"]
        user.github = self.cleaned_data["github"]
        user.bio = self.cleaned_data["bio"]
        user.skills = self.cleaned_data["skills"]
        user.experience = self.cleaned_data["experience"]
        user.education = self.cleaned_data["education"]
        
        if commit:
            user.save()
        return user

class UserPostForm(forms.ModelForm):

    expire_date = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserPost
        fields= ["title", "job_type", "city", "state", "preferred_skills", "description", "company", "expire_date", "status"]


class FavoritePost(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['favorites']

class InterestedCandidatesForm(forms.Form):
    # define field that uses the CheckboxSelectMultiple widget
    interested_candidates = forms.MultipleChoiceField(
        label='Interested Candidates (and their compatability score)',
        widget=forms.CheckboxSelectMultiple
    )
    salary = forms.CharField(label='Yearly Salary', max_length=50, required=True)
    deadline = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=True)


    def __init__(self, *args, **kwargs):
        # Get the list of choices from the keyword arguments
        choices = kwargs.pop('choices', None)

        # Initialize the form
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = True


        # Set the choices property of the my_field field to the list of choices
        self.fields['interested_candidates'].choices = choices

