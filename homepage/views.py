from django.shortcuts import render
from django.http import HttpResponse
from .models import Education, PythonProjects, WebProject

# Create your views here.


def home(request):
    details={ 'name':'Mohammed Sahir Anas',
    'profession':'Python Django Full Stack Developer',
    'location':'Malappuram District, Kerala, India',
    'quote':'If people are doubting how far I can go,I will go so far that I can’t hear them anymore'}

    projectsHeading={1:'Python Projects',2:'Web Design'}
   
    education=Education.objects.all()
    python=PythonProjects.objects.all()
    web=WebProject.objects.all()

    return render(request,'index.html',{
        'details':details,
        'education':education,
        'projectsHeading':projectsHeading,
        'webProjects':web,
        'pythonProjects':python
        })
