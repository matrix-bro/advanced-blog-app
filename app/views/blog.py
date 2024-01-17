from django.shortcuts import render, get_object_or_404
from app.models.blog import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.views.generic import ListView

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

    # Pagination with {2} posts per page
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page', 1)
    
    try:
        page_range = paginator.get_elided_page_range(number=page_number, on_each_side=1, on_ends=2)
        posts = paginator.page(page_number)
    except InvalidPage:
        # Handling All Exceptions (PageNotAnInteger, EmptyPage) Here

        page_range = paginator.get_elided_page_range(number=1, on_each_side=1, on_ends=2)
        posts = paginator.page(1)
        page_number = 1

    return render(request, 'app/blog/list.html', {
        "posts": posts,
        "page_range": page_range,
        'page_number': int(page_number),
    })

class PostListView(ListView):
    queryset = Blog.published.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'app/blog/list.html'


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Blog, slug=slug, created_at__year=year, created_at__month=month,created_at__day=day, status=Blog.StatusType.PUBLISHED)
    
    return render(request, 'app/blog/detail.html', {
        'post': post,
    })