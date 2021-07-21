from django.shortcuts import render, redirect
from .models import Blog, Author
from .forms import BlogForm, UserRegistrationsForm
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, './blogs/index.html')


@login_required
def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/all_blogs.html', {
        'blogs': blogs,
    })


@login_required
def detail_blogs(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blogs/detail_blog.html', {
        'blog': blog
    })


@login_required
def write_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            new_author = Author(user_name=request.user.username,
                                email=request.user.email)
            new_author.save()
            print("Author = ", request.user.email)
            new_blog = Blog(author=new_author, title=request.POST['title'],
                            excerpt=request.POST['excerpt'], content=request.POST['content'], date=date.today())
            new_blog.save()
            return redirect('all-blogs')
        else:
            return render(request, 'blogs/create.html', {
                'form': form
            })

    form = BlogForm()
    return render(request, 'blogs/create.html', {
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationsForm()
        return render(request, 'blogs/register.html', {
            'form': form
        })
