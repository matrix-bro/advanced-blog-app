from django.shortcuts import render, get_object_or_404
from app.forms import PostShareForm
from app.models.blog import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.views.generic import ListView
from django.core.mail import send_mail

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
    paginator = Paginator(posts, 2)
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

def post_share(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=Blog.StatusType.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = PostShareForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data

            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n"
            message += f"{cd['name']}'s comments: {cd['comments']}"
            
            send_mail(subject=subject, message=message, from_email='advblog@gmail.com', recipient_list=[cd['to']], fail_silently=False)

            sent = True

    else:
        form = PostShareForm()

    return render(request, 'app/blog/share.html', {
        'form': form,
        'post': post,
        'sent': sent
    })