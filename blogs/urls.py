from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-blogs', views.all_blogs, name='all-blogs'),
    path('all-blogs/<int:pk>', views.detail_blogs, name='detail_blogs'),
    path('write-blog', views.write_blog, name='write_blog'),
    path('profile', views.profile, name='profile')
]
