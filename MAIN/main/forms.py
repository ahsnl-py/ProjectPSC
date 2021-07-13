from django import forms
from django.forms.widgets import Select
from .models import Post, UploadFiles


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =  ['title', 'content', 'categories']

        labels = {
            'title': 'Title'
            , 'content': 'Body'
            , 'categories': 'categories'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'name':"post_title",
                'type':"text",
                'class':"form-control",
                # 'id':"exampleFormControlInput1",
                'placeholder':"Title",}),
            
            'content': forms.Textarea(attrs={
                'name':"post_text",
                'type':"text",
                # 'class':"editable medium-editor-textarea",
                'class': "form-control",
                # 'id':"exampleFormControlTextarea1",
                'placeholder':"Text",}),

            'categories':forms.Select(attrs={'class':'form-control'}),
        }

class NewPostUploads(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields =  ('file_upload',)

        widgets = {
            'file_upload': forms.ClearableFileInput(attrs={
                'name':"file",
                'type':"file",
                'multiple': True}),
        }