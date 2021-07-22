from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm, UserRegistrationsForm
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, './blogs/index.html')


def all_blogs(request):
    blogs = Blog.objects.all().order_by("-date")
    return render(request, 'blogs/all_blogs.html', {
        'blogs': blogs,
        'show_delete': False
    })


def delete_blog(request, pk):
    Blog.objects.get(id=pk).delete()
    return redirect('all-blogs')


@login_required
def detail_blogs(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blogs/detail_blog.html', {
        'blog': blog,
        'show_delete': True
    })


@login_required
def write_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = Blog(author=request.user, title=request.POST['title'],
                            excerpt=request.POST['excerpt'], content=request.POST['content'],
                            date=date.today())
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


@login_required
def profile(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blogs/profile.html', {
        'blogs': blogs
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationsForm(request.POST)

        if form.is_valid():
            form.save()
            print('Form', form)
            username = form.cleaned_data.get('username')
            print(f'Account successfully created for {username}!!')
            return redirect('login')
        else:
            return render(request, 'blogs/register.html', {
                'form': form
            })
    else:
        form = UserRegistrationsForm()
        return render(request, 'blogs/register.html', {
            'form': form
        })
