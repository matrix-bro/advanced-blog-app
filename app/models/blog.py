from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Blog.StatusType.PUBLISHED)


class Blog(models.Model):
    class StatusType(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISHED = 'Published'
        DELETED = 'Deleted'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="blog_posts")
    content = models.TextField()
    status = models.CharField(max_length=20, choices=StatusType.choices, default=StatusType.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()      # Default manager
    published = PublishedManager() # custom manager for getting published blog posts.

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created_at.year, self.created_at.month, self.created_at.day, self.slug])
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True) # filter inappropriate comments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return f"Comment by {self.name} on {self.blog}"