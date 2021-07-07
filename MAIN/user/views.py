from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

from .forms import UserRegisterForm


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

def signin(request):
    context = {}
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect("forum:home")
    context.update({
        "form": form
    })
    return render(request, "users/login.html", context)
