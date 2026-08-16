from django import forms
from .models import *



class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        exclude = ['user']



class JobseekerProfileForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['full_name','profile_photo','designation','gender','phone', 'email','location', 'about']



class AddJobseekerProfileform(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['certification','skills','experience','education']




class JobseekerUpdateForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['full_name','profile_photo', 'designation', 'phone', 'email', 'location',
            'resume', 'about', 'education', 'skills', 'experience', 'certification']




