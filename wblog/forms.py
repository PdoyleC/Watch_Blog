from .models import Comment, Post, Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'content')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
