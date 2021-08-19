from django.contrib import admin
from user.forms import UserRegisterForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import (
    CategoryDept
    , Category
    , Author
    , Post
    , Comment
    , Reply
    
)


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(CategoryDept)
admin.site.unregister(User)

@admin.register(User)
class NewUserAdmin(UserAdmin):
    add_form_template = 'screens/register.html'
    add_form = UserRegisterForm


