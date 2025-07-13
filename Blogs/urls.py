from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_list, name='blogs'),
    path('blog-detail/<id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('edit/<id>/', views.edit_blog, name='edit_blog'),
    path('delete/<id>/', views.delete_blog, name='delete_blog'),
    
]