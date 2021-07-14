from django.urls import path
from .views import ( 
    post_detail
    , department_subjects
    , post_list_by_categories
    , create_post
    , create_subject
)

app_name = 'forum'

urlpatterns = [
    path("", department_subjects, name="home"),
    path("posts/<slug>", post_list_by_categories, name="posts"),
    path("detail/<slug>/", post_detail, name="detail"),
    path("create_post/", create_post, name="create_post"),
    path("new_topic/", create_subject, name="create_subject"),
]