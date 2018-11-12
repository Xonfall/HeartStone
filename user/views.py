from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import MyCustomUserForm
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = MyCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if not (User.objects.filter(username=username).exists()):
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
    else:
        form = MyCustomUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)