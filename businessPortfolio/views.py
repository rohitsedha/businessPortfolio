from django.shortcuts import render

def home_view(request):
    return render(request, 'Home.html')

def about_view(request):
    return render(request, 'About.html')

def contact_view(request):
    return render(request, 'Contact.html')

def index_view(request):
    return render(request, 'index.html')
