from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from application.models import *
from .forms import *

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.



def profile_dashboard(request): 
    if request.user.role == 1:
        if Jobseeker.objects.filter(user=request.user).exists():
            profile = Jobseeker.objects.get(user=request.user)
            return render(request, 'jobseeker_profile.html',  {'profile': profile})
        else:
            return redirect('complete_profile')

    elif request.user.role == 2:
        if Employer.objects.filter(user=request.user).exists():
            profile = Employer.objects.get(user=request.user)
            return render(request, 'employer_profile.html', {'profile': profile})
        else:
            return redirect('complete_profile')
    else:
        return redirect('/')





def complete_profile(request):

    if request.user.role == 1:        # jobseeker   
        if request.method == 'POST':
            form = JobseekerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                a = form.save(commit=False)
                a.user = request.user
                a.save()
                return redirect('profile_dashboard')
        else:
            form = JobseekerProfileForm()
        return render(request, 'complete_jobsee_profile.html', {'form': form})

    else:                           # employer
        if request.method == 'POST':
            form = EmployerProfileForm(request.POST, request.FILES)
            if form.is_valid():
                a = form.save(commit=False)
                a.user = request.user
                a.save()
                return redirect('profile_dashboard')
        else:
            form = EmployerProfileForm()
        return render(request, 'complete_emp_profile.html', {'form': form})


        
def addJobseeprofile_details(request):
    jobseeker = Jobseeker.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddJobseekerProfileform(request.POST, instance=jobseeker)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('profile_dashboard')
    else:
        form = AddJobseekerProfileform(instance=jobseeker)
    return render(request, 'addJobseeprofile_details.html', {'form': form})




def update_profile(request):

    if request.user.role == 1:
        jobseeker = Jobseeker.objects.get(user=request.user)

        if request.method == 'POST':
            form = JobseekerUpdateForm(request.POST, request.FILES, instance=jobseeker)
            if form.is_valid():
                a = form.save(commit=False)
                a.user = request.user
                a.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile_dashboard')
        else:
            form = JobseekerUpdateForm(instance=jobseeker)
        return render(request, 'update_jobseeker_profile.html', {'form': form})

    elif request.user.role == 2:
        employer = Employer.objects.get(user=request.user)

        if request.method == 'POST':
            form = EmployerProfileForm(request.POST, request.FILES, instance=employer)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile_dashboard')
        else:
            form = EmployerProfileForm(instance=employer)
        return render(request, 'update_employer_profile.html', {'form': form})

    else:
        messages.error(request, 'Invalid user role')
        return redirect('login')






