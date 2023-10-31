from django.shortcuts import render, get_object_or_404
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post
from .forms import EmailPostForm

class PostListView(ListView):
    """
    Class Based View for post list
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginated_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request:HttpRequest, year:int, month:int, day:int, post:str) -> HttpResponse:
    post:Post = get_object_or_404(Post,
                                  status=Post.Status.PUBLISHED,
                                  slug=post,
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=post.status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Send Email\
    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form})
