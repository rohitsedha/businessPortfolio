from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/post.html', {'post': post})

# Static views 
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'About.html')

def contact_view(request):
    return render(request, 'Contact.html')

def index_view(request):
    return render(request, 'index.html')

def courses_view(request):
    return render(request, 'course.html')

def courses1_view(request):
    return render(request, 'course1.html')

def courses2_view(request):
    return render(request, 'course2.html')

def courses3_view(request):
    return render(request, 'course3.html')


def discover_view(request):
    return render(request, 'discover.html')