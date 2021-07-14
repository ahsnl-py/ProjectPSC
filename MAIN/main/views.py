from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Author, Comment, Post, Category, UploadFiles, Reply
from .utils import update_views
from .forms import NewPost, NewPostUploads



def department_subjects(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "screens/department_subjects.html", context)

def all_forums(request):
    posts = Post.objects.all()

    return redirect(request, "components/navbar.html", {'posts':posts})

def post_list_by_categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts": posts,
        "forum": category,
    }
    return render(request, "screens/post_list.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    user = Author.objects.get(user=request.user)

    # for c in post.comments.all():
    #     if c.count != 0:
    #         replies = [r for r in c.replies.all()]

    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=user, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        comment_id =  request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user=user, content=reply)
        comment_obj.replies.add(new_reply.id)

    
    context = {
        "post": post, 
        "totl_comment": post.num_comments 
    }
    update_views(request, post)
    return render(request, "screens/post_detail.html", context)

@login_required
def create_post(request):
    context = {}
    user = request.user
    form = NewPost(request.POST or None) 
    file_upload = NewPostUploads(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if request.method == 'POST':
        if form.is_valid() and file_upload.is_valid():
            author = Author.objects.get(user=user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.approved = True
            new_post.save()
            for f in files:
                file_instance = UploadFiles(file_upload=f, feed=new_post)
                file_instance.save()
            return redirect('forum:home')


    context.update({
        'form':form,
        'upload':file_upload
    })
    
    return render(request, 'screens/post_create.html', context)
