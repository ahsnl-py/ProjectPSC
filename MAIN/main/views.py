""" Things To do:
> forget passwords

"""
# FUNCTIONS AND METHODS START HERE....
from genericpath import exists
import os 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from .utils import update_views

# inHouse import Class 
from .forms import (
    NewPost, NewPostUploads, NewSubject
)
from .models import (
        Author, Comment, Post, Category, UploadFiles, Reply,
        CategoryDept
)

#Will be deleted
def test_subject_list(request):
    subjects = Category.objects.all()
    context = {
        "subjects":subjects,
    }
    return render(request, "screens/test_subjects_list.html", context)


# Home page 
def department_subjects(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "screens/department_subjects.html", context)

# Sidebar functionality
def subject_list_by_department(request, dept_id):
    context = {}
    dept_all = [t.id for t in CategoryDept.objects.all()] 
    if dept_id in dept_all:
        subjects_all = Category.objects.filter(deptartment=dept_id)

    context.update ({
        'subject_filter_by_dept':subjects_all
    })

    return render(request, "screens/subject_list.html", context)

# List all forums (post) in a page
def post_list_all(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, "screens/post_list_all.html", context)

# List all forums (post) by department in a page 
def post_list_categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts": posts,
        "forum": category,
    }
    return render(request, "screens/post_list_categories.html", context)

# Detail of a forum (post) in a page
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(post)
    user = Author.objects.get(user=request.user)
    print(user)

    # get extension name
    # list_extension_type = []
    list_extension_type = ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', 'jpg', 'png']
    feed_upload = UploadFiles.objects.filter(feed=post.id)
    file_name = [f.file_upload.name for f in feed_upload]
    file_extensions = [os.path.splitext(f)[1].lower() for f in file_name]
    extension_type = {'images': [], 'docs': []}
    
    for f, ext in zip(feed_upload, file_extensions):
        if ext in ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt']:
            extension_type['docs'].append(f)
        elif ext in ['.jpg', '.png']:
            extension_type['images'].append(f)

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
        "uploads": feed_upload,
        "extension": extension_type,
        "totl_comment": post.num_comments 
    }
    update_views(request, post)
    return render(request, "screens/post_detail.html", context)


@login_required(login_url='user:login')
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

@login_required(login_url='user:login')
def create_subject(request):
    context = {}
    new_subject = NewSubject(request.POST or None)
    if request.method == "POST":
        if new_subject.is_valid():
            new_category = new_subject.save(commit=False)
            new_category.save()
            return redirect('forum:home')
    
    context.update ({
        'new_subject': new_subject
    })

    return render(request, 'screens/subject_create.html', context)

def search_result(request):

    return render(request, "screens/subject_search.html")
# !FUNCTIONS AND METHODS END HERE!

""" 
 ### MAJOR UPDATES NEEDS TO BE LOGGED: ###
-----------------------------------------------
user    descriptions                    ticket
-----------------------------------------------
"""