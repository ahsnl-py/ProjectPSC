from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Author 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email',)
 
    # widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control'}),
    #         'email': forms.EmailInput(attrs={'class': 'form-control'}),   
    #         'password1': forms.PasswordInput(attrs={'class': 'form-control'}),   
    #         'password2': forms.PasswordInput(attrs={'class': 'form-control'}),            
    #     }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Author 
        fields = ['fullname', 'user', 'bio', 'profile_pic']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),            
        }



