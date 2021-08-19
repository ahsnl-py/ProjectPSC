from django.http.response import Http404
from django.views import generic 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateForm
from django.urls import reverse_lazy
from main.models import Author

class Register(generic.CreateView): 
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url =  reverse_lazy('user:login')

def signup(request):
    context = {}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            #username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            #user.is_active = False
            user.save()
            login(request, user)
            return redirect("forum:home")
    else:
        form = UserRegisterForm()

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
    
    try:
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
    except UnboundLocalError:
        raise "Create an User info first" 
    
    finally:
        context.update({
            "form": form,
            "user": user_info
        })
    return render(request, "users/profile_update.html", context)






