from django.urls import path
from .views import register, signup, signin

app_name = 'user'

urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', signin, name='login'),
]