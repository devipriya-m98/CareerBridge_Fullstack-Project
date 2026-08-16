from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import *
from application.models import *
from django.db.models import Q
from .forms import *
from django.http import HttpResponseForbidden



# Create your views here.


def jobs_list(request):
    jobs = Job.objects.all().order_by('-id')

    paginator = Paginator(jobs, 4)
    page_number = request.GET.get('page')
    jobs_final = paginator.get_page(page_number)
    return render(request, 'jobs_list.html', {'jobs': jobs_final})



def job_details(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_details.html', {'job': job})


def category_view(request,id):
    jobs = Job.objects.filter(category_id=id)
    return render(request, 'category_view.html', {'jobs': jobs})


def search(request):
    a = request.GET.get('q', '')
    results = Job.objects.filter(
        Q(job_title__icontains=a)|
        Q(location__icontains=a)|
        Q(skills__icontains=a))
    return render(request,'search.html',{'results': results})



@login_required(login_url="/login")
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)

        if form.is_valid():
            a = form.save(commit=False)
            a.employer = request.user
            a.save()
            messages.success(request, "Job added Successfully!")
            return redirect('manage_job')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})



@login_required
def manage_job(request):
    jobs = Job.objects.filter(employer=request.user)
    return render(request, 'manage_job.html',{'jobs': jobs})



@login_required
def update_job(request,id):
    job = get_object_or_404(Job, id=id)

    if job.employer != request.user:
        return HttpResponseForbidden("You are not allowed to edit this job")

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job details updated!")
            return redirect('manage_job')
    else:
        form = JobForm(instance=job)

    return render(request, 'post_job.html', {'form': form})



@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == 'POST':
        job.delete()
        messages.success(request, "Job deleted successfully!")
        return redirect('manage_job')

    return render(request, 'delete_job.html', {'job': job})