from django.shortcuts import render, redirect
from django.contrib import messages

from profile_app.models import *

from django.contrib.auth import get_user_model, authenticate, login, logout


User = get_user_model()

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        u = request.POST['u_name']
        p = request.POST['password']
        user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)

            if user.role == 1:
                if Jobseeker.objects.filter(user=user).exists():
                    return redirect('/')
                else:
                    return redirect('complete_profile')

            elif user.role == 2:
                if Employer.objects.filter(user=user).exists():
                    return redirect('/')
                else:
                    return redirect('complete_profile')
        else:
            messages.error(request, '*Invalid Username or Password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        u = request.POST['u_name']
        e = request.POST['email']
        p = request.POST['password']
        role = request.POST.get('role')

        if User.objects.filter(username=u).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        elif User.objects.filter(email=e).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')
        
        User.objects.create_user(username=u, email=e, password=p, role=role)
        messages.success(request, 'Registered successfully! Please log in.')
        return redirect('login')
    
    return render(request, 'register.html')