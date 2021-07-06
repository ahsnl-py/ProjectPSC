from django.urls import path
from .views import home, post_detail, post_list
urlpatterns = [
    path("", home, name="home"),
    path("posts/<slug>", post_list, name="posts"),
    path("detail/<slug>/", post_detail, name="detail"),
]