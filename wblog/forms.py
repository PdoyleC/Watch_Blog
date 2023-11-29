from .models import Comment, Post, Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Form for posting a new Alert


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(attrs={'class':
                                                              'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
