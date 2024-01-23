from django.contrib.sitemaps import Sitemap
from app.models.blog import Blog

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Blog.published.all()
    
    def lastmod(self, obj):
        return obj.updated_at