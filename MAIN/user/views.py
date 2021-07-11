from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateForm
from main.models import Author


def register(request):
    context = {}
    form = UserRegisterForm()
    #UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("forum:home")
    context.update({
        "form": form, 
        "title": "Register"
    })
    return render(request, 'users/register.html', context)


def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("forum:home")
    context.update({
        "form": form, 
        "title": "Signup",
    })
    return render(request, 'users/register.html', context)

def profile(request):
    context = {}
    return render(request, "users/profile.html", context)

@login_required
def update_profile(request):
    context = {}
    user = request.user 
    user_info = Author.objects.get(user=user)
    form = UpdateForm(request.POST, request.FILES, use_required_attribute=False)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user 
            update_profile.save()
            return redirect("forum:home")
        
    context.update({
        "form": form,
        "user": user_info
    })
    return render(request, "users/profile_update.html", context)






