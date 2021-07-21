from django.shortcuts import render
from .models import Blog
from .forms import  BlogForm


# Create your views here.

def home(request):
    return render(request, './blogs/index.html')


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/all_blogs.html', {
        'blogs': blogs,
    })


def detail_blogs(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blogs/detail_blog.html', {
        'blog': blog
    })


def write_blog(request):
    form = BlogForm()
    return render(request, 'blogs/create.html', {
        'form' : form
    })
