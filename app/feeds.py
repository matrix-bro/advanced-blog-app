from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from app.models.blog import Blog
from django.template.defaultfilters import safe, truncatewords_html, striptags

class LatestPostsFeed(Feed):
    title = 'Expressit Blogs'
    link = reverse_lazy('posts')
    description = 'Latest posts'

    def items(self):
        return Blog.published.all()[:5]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords_html(safe(striptags(item.content)), 10)

    def item_pubdate(self, item):
        return item.created_at