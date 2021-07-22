from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.SET("Anonymous"), related_name='blogs')
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title
