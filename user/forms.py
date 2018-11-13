from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm


class MyCustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}

    def save(self, commit=True):

        user = super(MyCustomUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
