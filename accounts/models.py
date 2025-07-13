from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('enroller', 'Enroller'),
        ('student', 'Student'),
        ('guest','Guest'),
    
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')

