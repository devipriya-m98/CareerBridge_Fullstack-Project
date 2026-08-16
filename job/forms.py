from django import forms
from .models import *


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['job_logo','sub_category','created_at','updated_at','is_featured','employer']