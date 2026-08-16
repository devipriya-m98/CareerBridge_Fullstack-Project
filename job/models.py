from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Categories/')
    def __str__(self):
        return self.title


class Industry(models.Model):
    industry_type =  models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.industry_type} - ({self.category.title})"



class Job(models.Model):
    
    jobtype_choices = (
        ('Full-time', 'Full time'),
        ('Part-time', 'Part time'),
        ('Temporary', 'Temporary'),
        ('Freelance', 'Freelance'),
    )
    work_location_choices = (
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
    )

    job_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to='company_logos', null=True, blank=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=jobtype_choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    industry_type = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    responsibilities = models.TextField()
    skills = models.TextField()
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    experience = models.TextField(max_length=50)
    work_location = models.CharField(max_length=50, choices=work_location_choices)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.job_title}"