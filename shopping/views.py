import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Card
from cards.models import User_cards
from user.models import User


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
                user_money = user_money - price
                if user_money >= 0:
                    User(id=user_id, money=user_money).save()
                    cards = [
                        Card.objects.get(id=random.randint(1, 499)),
                        Card.objects.get(id=random.randint(1, 499)),
                        Card.objects.get(id=random.randint(1, 499))
                    ]
                    user_card_registery = User_cards.objects.create(
                        user=User(id=user_id)
                    )
                    user_card_registery.save()

                    for card in cards:
                        user_card_registery.card.add(card)

                    return render(request, 'shopping/index.html')
                else:
                    return render(request, 'shopping/index.html')
            elif choice == 'choice2':
                price = 150
                print()
            elif choice == 'choice3':
                price = 300
                print()
