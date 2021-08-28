from django.shortcuts import render
from .models import *


def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects})