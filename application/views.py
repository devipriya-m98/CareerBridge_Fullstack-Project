from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from job.models import *

from .forms import *

from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="/login")
def apply_job(request, id):
    job = Job.objects.get(id=id)
    
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, "You have already applied for this job.")
        return redirect('jobs_list')

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job = job
            application.save()
            messages.success(request, "Your Application submitted Successfully!!")
            return redirect('my_application')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {"form": form, 'job':job})


@login_required
def my_application(request):
    application = Application.objects.filter(applicant=request.user)
    return render(request, 'my_application.html', {'application': application})



@login_required
def view_applicants(request, id):
    job = Job.objects.get(id=id, employer=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'view_applicants.html', {'job': job, 'applications': applications})



@login_required
def all_applicants(request):
    applications = Application.objects.filter(job__employer=request.user)
    return render(request, 'all_applicants.html', {'applications': applications})


@login_required
def update_status(request,id):
    application = Application.objects.get(id=id)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Status updated..!")
            return redirect('all_applicants')
    else:
        form = StatusForm()
    return render(request, 'update_status.html', {'form': form})