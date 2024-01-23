from django.urls import path
from app.views import blog
from app.feeds import LatestPostsFeed

urlpatterns = [
    path('', blog.index, name='index'),
    path('posts/', blog.posts, name='posts'),
    path('posts/tag/<slug:tag_slug>/', blog.posts, name='post_list_by_tag'),
    # path('posts/', blog.PostListView.as_view(), name='posts'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', blog.post_detail, name='post_detail'),

    path('post/<slug:slug>/share/', blog.post_share, name='post_share'),
    path('post/<slug:slug>/comment/', blog.post_comment, name='post_comment'),

    # feed
    path('blog/feed/', LatestPostsFeed(), name='post_feed'),

]
