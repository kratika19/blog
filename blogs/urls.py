from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-blogs', views.all_blogs, name='all-blogs'),
]
