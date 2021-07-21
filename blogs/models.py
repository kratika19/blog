from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Author(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user_name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET("Anonymous"), related_name='blogs')
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title
