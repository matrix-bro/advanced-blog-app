from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    class StatusType(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISHED = 'Published'
        DELETED = 'Deleted'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="blog_posts")
    content = models.TextField()
    status = models.CharField(max_length=20, choices=StatusType.choices, default=StatusType.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.title