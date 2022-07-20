from django import forms
from .models import DevTool, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','content','interest','devtool']

class ToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']