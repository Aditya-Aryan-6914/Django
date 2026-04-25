from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'search_description', 'tags', 'images', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'search_description': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }