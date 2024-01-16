from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

]
