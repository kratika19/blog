from django import forms
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
