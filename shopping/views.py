import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Card


# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')


@login_required
def buy_cards(request):
    if request.method == 'POST':
        user_money = request.user.money
        username = request.user
        user_id = request.user.id

        if request.POST['choice'] is not None:
            choice = request.POST['choice']

            if choice == 'choice1':
                price = 50
                cards = Card.objects.all().get(id=random.randint(1, 499))
                print(cards)
            elif choice == 'choice2':
                price = 150
                print()
            elif choice == 'choice3':
                price = 300
                print()
