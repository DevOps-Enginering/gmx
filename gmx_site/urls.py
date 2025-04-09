from django.urls import path
from .views import home
from . import views
from django.contrib import admin
from django.urls import path
from gmx_site.views import home, blog


urlpatterns = [
    path('', home),
     path('blog/', views.blog, name='blog'),
]
