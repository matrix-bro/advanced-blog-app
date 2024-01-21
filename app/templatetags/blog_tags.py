from django import template
from app.models.blog import Blog

register = template.Library()

@register.simple_tag
def total_posts():
    return Blog.published.count()

@register.inclusion_tag('app/blog/includes/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Blog.published.order_by('-created_at')[:count]
    return {'latest_posts': latest_posts}