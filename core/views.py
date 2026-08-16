from django.shortcuts import render, redirect

from job.models import *

# Create your views here.


def home(request):
    categories = Category.objects.all()
    featured_jobs = Job.objects.filter(is_featured=True)
    context = {
        'categories':categories,
        'jobs': featured_jobs
    }
    return render(request,'home.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





