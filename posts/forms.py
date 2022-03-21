from django.forms import ModelForm
from django import forms
from .models import Post, PostComment


class PostCreateForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'desc', 'contact', 'location', 'image', 'category']

class PostCommentForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Leave Your comments.',
        'class': 'form-control',
        'rows': '5'
        
    }))
    
    class Meta:
        model = PostComment
        fields = ['content']