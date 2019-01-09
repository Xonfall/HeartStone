import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Card
from user.models import User


# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')


@login_required
def buy_cards(request):
    if request.method == 'POST':
        

                    return render(request, 'shopping/index.html')
            
