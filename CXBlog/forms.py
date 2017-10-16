#coding:utf-8
from django import forms
from .models import Comment

# 发送邮件的表单
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                                         widget=forms.Textarea)
# 评论的表单
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


from .models import Post
from pagedown.widgets import AdminPagedownWidget
from django import forms
class BlogForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Post
        fields = '__all__'