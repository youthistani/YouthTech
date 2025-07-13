from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    auther = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.title} {self.auther}' 


class Comments(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    auther = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments By {self.auther}"