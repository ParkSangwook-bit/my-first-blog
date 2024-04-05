from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# 이 폼은 Post 모델에 대한 폼이며, title과 text 필드를 가지고 있습니다.

class test(forms.ModelForm):
    class Meta:
        test = Post
        fields = ('author', 'created_date',)