from django.shortcuts import render, get_object_or_404
from django.db.models.query import QuerySet
from django.http import HttpResponse

from .models import Post

def post_list(request) -> HttpResponse:
    posts:QuerySet = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id) -> HttpResponse:
    post:Post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})