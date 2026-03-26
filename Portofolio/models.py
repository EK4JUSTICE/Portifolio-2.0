from django.db import models
from django.conf import settings
import os

def project_image_path(instance, filename):
    """Generate file path for project images"""
    return f'projects/{instance.title.replace(" ", "_").lower()}/{filename}'

def profile_image_path(instance, filename):
    """Generate file path for profile images"""
    return f'profile/{filename}'

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Graphic Design'),
        ('development', 'Full Stack Development'),
        ('both', 'Design & Development'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to=project_image_path, default='projects/placeholder.jpg')
    link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Profile(models.Model):
    """Model for storing profile information and images"""
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=200, default="Graphics Designer & Full Stack Developer")
    bio = models.TextField(default="Professional profile description")
    profile_image = models.ImageField(upload_to=profile_image_path, default='profile/default.svg')
    email = models.EmailField(default="your.email@example.com")
    phone = models.CharField(max_length=20, default="+1 (234) 567-890")
    location = models.CharField(max_length=100, default="Your City, Your Country")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    proficiency = models.IntegerField(default=80)

    def __str__(self):
        return self.name
