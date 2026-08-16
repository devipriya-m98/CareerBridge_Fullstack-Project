from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.



class Jobseeker(models.Model):

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to= 'jobseeker_profile_photo/', null=True, blank=True)
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=15, choices=gender_choices)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.CharField(max_length=50)
    resume = models.FileField(upload_to='jobseeker resumes/', null=True, blank=True)
    about = models.TextField(max_length=300)
    education = models.TextField()
    skills = models.TextField()
    experience = models.TextField(null=True, blank=True)
    certification = models.TextField()
    def __str__(self):
        return self.full_name




class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to= 'employer_profile_photo/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    company_name = models.CharField(max_length=30)
    company_logo = models.ImageField(upload_to='employer_company_logos/', null=True, blank=True)
    about_company = models.TextField()
    company_website = models.URLField()
    company_type = models.CharField(max_length=50)
    def __str__(self):
        return self.full_name