from django.urls import path
from .views import home, post_detail, post_list, department_subjects, test_post_list
urlpatterns = [
    #path("", home, name="home"),
    path("", department_subjects, name="home"),
    path("posts/<slug>", test_post_list, name="posts"),
    #path("posts/<slug>", post_list, name="posts"),
    path("detail/<slug>/", post_detail, name="detail"),
]