from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render
from .models import Author, Comment, Post, Category
from .utils import update_views



def department_subjects(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "screens/department_subjects.html", context)

def test_post_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts": posts,
        "forum": category,
    }

    return render(request, "screens/post_list.html", context)


def home(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "forums.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post
    }
    update_views(request, post)
    return render(request, "screens/post_detail.html", context)

class PostCreateView(CreateView):
    model = Post 
    fields = ('title', 'categories', 'content')
    template_name = 'screens/post_create.html'


# def new_post(request):
#     form = NewPost()
#     upload = NewPostUploads()
#     if request.method == 'POST':
#         form = NewPost(request.POST,)
#         if form.is_valid():
#             new_post = form.save(commit=False)
#             new_post.author = request.user
#             new_post.status = 'published'
#             new_post.save()
#             return redirect('forum:forum_post_list')
#         else:
#             pass
    
#     return render(request, 'forum/new_post.html', {'form':form, 'upload':upload})
