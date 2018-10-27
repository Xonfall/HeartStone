from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


class CardForm(ModelForm):

    @login_required
    def index(request):
        return render(request, 'index.html')
