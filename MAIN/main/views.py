
from django.shortcuts import get_object_or_404, render
from .models import Author, Post, Category
from .utils import update_views


def home(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "forums.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post.comments)
    context = {
        "post": post
    }
    update_views(request, post)
    return render(request, "detail.html", context)

def post_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts": posts,
        "forum": category,
    }

    return render(request, "posts.html", context)