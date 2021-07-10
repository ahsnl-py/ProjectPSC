

# class NewPost(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields =  ('title', 'body','subject_name')

#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'name':"post_title",
#                 'type':"text",
#                 'class':"form-control",
#                 'id':"exampleFormControlInput1",
#                 'placeholder':"Title",}),
            
#             'body': forms.Textarea(attrs={
#                 'name':"post_text",
#                 'type':"text",
#                 # 'class':"editable medium-editor-textarea",
#                 'class': "form-control",
#                 'id':"exampleFormControlTextarea1",
#                 'placeholder':"Text",}),
#         }