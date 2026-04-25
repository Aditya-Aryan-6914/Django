from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('post/<int:post_id>/', views.blog_post, name='blog_post')
] 
