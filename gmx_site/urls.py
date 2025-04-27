from django.urls import path
from .views import home
from . import views
from django.contrib import admin
from django.urls import path
from gmx_site.views import home, about, contact, projects


urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
]
