from django.shortcuts import render, get_object_or_404
from app.models.blog import Blog

def index(request):
    # Today's top 2 posts
    # TODO: Different query
    today_two_posts = Blog.published.all()[:2]

    # Today's main post
    # TODO: Different query
    today_main_post = Blog.published.first()
    
    # Recent Five Posts
    # TODO: Different query
    posts = Blog.published.all()[:5]

    print(today_main_post)

    return render(request, 'app/index.html', {
        "today": today_two_posts,
        "today_main": today_main_post,
        "posts": posts,
    })

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