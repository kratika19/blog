from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    # author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')
