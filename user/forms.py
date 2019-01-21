from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import User


class MyCustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2', 'email'}

    def save(self, commit=True):

        user = super(MyCustomUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']