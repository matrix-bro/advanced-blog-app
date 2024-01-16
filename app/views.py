from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from app.models.blog import Blog

def index(request):
    return HttpResponse("<h1>hello django</h1>")

def posts(request):
    posts = Blog.published.all()

    return render(request, 'app/blog/list.html', {
        "posts": posts,
    })

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=Blog.StatusType.PUBLISHED)
    
    return render(request, 'app/blog/detail.html', {
        'post': post
    })