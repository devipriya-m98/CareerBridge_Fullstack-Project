from django import forms
from .models import *



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['applicant', 'job', 'status']



class StatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']
