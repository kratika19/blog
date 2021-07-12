from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, './blogs/index.html')


def all_blogs(request):
    return render(request, 'blogs/all_blogs.html')
