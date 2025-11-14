from django.shortcuts import render
from django.http import JsonResponse
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    for project in projects:
        project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
    return render(request, 'portfolio.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
    return render(request, 'project_detail.html', {'project': project})
