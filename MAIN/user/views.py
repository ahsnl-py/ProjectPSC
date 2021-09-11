from django.http.response import Http404
# from django.urls.base import reverse
from django.urls import reverse
from django.views import generic, View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UpdateForm
from django.urls import reverse_lazy
from main.models import Author
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

from django.contrib.auth.models import User

class Register(generic.CreateView): 
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url =  reverse_lazy('user:login')

def signup(request):
    context = {}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            domain = get_current_site(request).domain
            link = reverse('user:activate', kwargs={'uidb64': uidb64, 'token': token})

            activate_url = 'http://' + domain + link

            email_subject = "Account Activation"
            email_body = f"Hi {user.username}, Please use the following link to activate your account\n {activate_url}"

            email = EmailMessage(
                email_subject,
                email_body,
                'praguestudentcenter@gmail.com',
                [user.email],
            )
            email.send(fail_silently=False)

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


class VerificationView(View):
    def get(self, request, uidb64, token):
        p = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=p)
        user.is_active = True
        user.save()
        return redirect('user:login')




