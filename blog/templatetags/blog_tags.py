from django import template
from ..models import Post

register = template.Library()

@register.simple_tag(name='total_blog_posts')
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}