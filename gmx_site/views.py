from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')  

# def blog(request):
#     return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')