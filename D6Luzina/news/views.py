from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.utils import timezone


class NewsList(ListView):
    model = Post
    template_name = 'posts/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')


class NewsDetail(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'news_details'