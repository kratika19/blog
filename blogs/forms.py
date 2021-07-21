from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'excerpt', 'content']
        # exclude = ['post']
        labels = {
            "title": "Enter title of your blog",
            "excerpt": "Enter what you are writing about in brief",
            "content": "Write your views"
        }


class UserRegistrationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
