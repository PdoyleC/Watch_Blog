from .models import Comment, Post, Contact, VideoPost
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


class VideoPostForm(forms.ModelForm):
    class Meta:
        model = VideoPost
        fields = ('title', 'video', 'content')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
