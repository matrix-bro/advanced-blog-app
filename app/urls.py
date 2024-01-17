from django.urls import path
from app.views import blog

urlpatterns = [
    path('', blog.index, name='index'),
    path('posts/', blog.posts, name='posts'),
    # path('posts/', blog.PostListView.as_view(), name='posts'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', blog.post_detail, name='post_detail'),

]
