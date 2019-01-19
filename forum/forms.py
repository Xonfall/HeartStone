from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from forum.models import Forum, Topic, Post
from user.models import User
from django import forms


class TopicForm(ModelForm):
    class Meta:
        model = Topic

        title = forms.CharField(
            label='title',
            max_length=100,
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=True
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Description du topic'}),
        }
        fields = ['title', 'description']


class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'comment': forms.Textarea(attrs={'required': True, 'rows': 4, 'placeholder': 'Commentaire'}),
        }
        fields = ['comment']
