"""
URL configuration for businessPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from businessPortfolio import views  # Import views from the businessPortfolio app
from django.views.generic import TemplateView 

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path('', views.blog_list, name='blog_list'), 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'), 
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('index/', views.index_view, name='index'),
    path('courses/', views.courses_view, name='courses'),
    path('whychooseus/', views.discover_view, name='discover'),
]
