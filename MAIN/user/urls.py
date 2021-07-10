from django.urls import path
from .views import register, signup, update_profile, profile
from django.contrib.auth import views as auth_views


app_name = 'user'

urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update', update_profile, name='update'),
]