from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.files.storage import default_storage
from .models import Project, Skill, Profile
from .forms import ProjectForm, ProfileForm

@require_http_methods(["GET"])
def home(request):
    """Home page with hero section and featured projects"""
    featured_projects = Project.objects.all()[:6]
    skills = Skill.objects.all().order_by('category')
    profile = Profile.objects.first()  # Get the first profile or None
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'profile': profile,
    }
    return render(request, 'home.html', context)

@require_http_methods(["GET"])
def projects(request):
    """Projects page with filtering"""
    category = request.GET.get('category', 'all')

    if category == 'all':
        projects_list = Project.objects.all()
    else:
        projects_list = Project.objects.filter(category=category)

    context = {
        'projects': projects_list,
        'current_category': category,
    }
    return render(request, 'projects.html', context)

@require_http_methods(["GET"])
def about(request):
    """About page"""
    skills = Skill.objects.all().order_by('category')
    profile = Profile.objects.first()
    context = {
        'skills': skills,
        'profile': profile,
    }
    return render(request, 'about.html', context)

@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact page"""
    profile = Profile.objects.first()
    if request.method == 'POST':
        # Handle form submission (you can add email functionality here later)
        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('portofolio:contact')

    context = {
        'profile': profile,
    }
    return render(request, 'contact.html', context)

@require_http_methods(["GET", "POST"])
def upload_project(request):
    """Upload new project with image"""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project uploaded successfully!')
            return redirect('portofolio:projects')
    else:
        form = ProjectForm()

    context = {
        'form': form,
        'title': 'Upload New Project',
    }
    return render(request, 'upload_project.html', context)

@require_http_methods(["GET", "POST"])
def upload_profile(request):
    """Upload or update profile information and image"""
    profile = Profile.objects.first()
    if not profile:
        profile = Profile()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('portofolio:home')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'title': 'Update Profile',
        'profile': profile,
    }
    return render(request, 'upload_profile.html', context)
