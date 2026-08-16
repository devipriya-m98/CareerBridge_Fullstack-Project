from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    role_choices = (
        (0, 'Admin'),
        (1, 'Job Seeker'),
        (2, 'Employer'),
    )
    role = models.IntegerField(default=0, choices=role_choices)

    def __str__(self):
        return f"{self.username}"
