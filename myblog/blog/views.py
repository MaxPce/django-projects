from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.filter(is_published=True).order_by('-date')
    context = {'posts': post_list}
    return render(request, 'blog/index.html',context)

def post(request, post_id):
    data = Post.objects.get(id=post_id)
    context = {'post': data}
    return render(request, 'blog/post.html', context)