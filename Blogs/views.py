from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import BlogPost, Category
from .forms import BlogPostForm, CommentsForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def blog_list(request):
    query = request.GET.get('q')
    cat_id = request.GET.get('category')
    posts = BlogPost.objects.all().order_by('-created_at')
    if query:
        posts = posts.filter(Q(title__icontains=query)|Q(content__icontains=query))
    if cat_id:
        posts = posts.filter(category_id=cat_id)
    

    paginater = Paginator(posts, 3) # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginater.get_page(page_number)

    featured_posts = BlogPost.objects.filter(featured=True).order_by('-created_at')[:3]


    categories = Category.objects.all()
    return render(request, 'blog.html', {
        'page_obj': page_obj,
        'categories': categories,
        'featured_posts': featured_posts
        })

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    comments = post.comments.all().order_by('-created_at')
    form = CommentsForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.auther = request.user
        comment.save()
        return redirect('blog_detail', post.id)
    return render(request, 'blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
        })

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.auther = request.user
            blog.save()
            return redirect('blog_detail', id=blog.id)
    else:
        form = BlogPostForm()
        return render(request, 'blog_form.html', {'form': form})
    

@login_required
def edit_blog(request, id):
    post = get_object_or_404(BlogPost, id=id, auther=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
        return render(request, 'blog_form.html', {'form': form, 'post': post})

@login_required
def delete_blog(request, id):
    post = get_object_or_404(BlogPost, id=id, auther=request.user)
    if request.method == 'post':
        post.delete()
        return redirect('blogs')
    else:
        return render(request, 'blog_delete_form.html', {'post': post})
