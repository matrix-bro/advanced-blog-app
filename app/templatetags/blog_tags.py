from django import template
from app.models.blog import Blog
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    return Blog.published.count()

@register.inclusion_tag('app/blog/includes/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Blog.published.order_by('-created_at')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Blog.published.annotate(total_comments=Count('comments')).filter(total_comments__gte=1).order_by('-total_comments')[:count]