from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-blogs', views.all_blogs, name='all-blogs'),
    path('all-blogs/<int:pk>', views.detail_blogs, name='detail_blogs')
]
