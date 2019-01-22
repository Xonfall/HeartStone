import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Card
from cards.models import Card_user
from user.models import User
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')


@login_required
def buy_cards(request):
    if request.method == 'POST':
        user_money = request.user.money
        username = request.user
        user_id = request.user.id
        cards = []

        if request.POST['choice'] is not None:
            choice = request.POST['choice']

            if choice == 'choice1':
                price = 50
                user_money = user_money - price

                if user_money >= 0:
                    User.objects.filter(id=user_id).update(money=user_money)
                    request.user.money = user_money

                    for i in range(0, 4):
                        cards.append(Card.objects.get(id=random.randint(1, 499)))

                    for card in cards:
                        Card_user(card_id=card.id, user_id=request.user.id).save()
                    messages.success(request, 'Vous avez acheter le pack starter')
                    return render(request, 'shopping/index.html')
                else:
                    messages.error(request, 'Vous n\'avez pas assez d\'argent.')
                    return render(request, 'shopping/index.html')
            elif choice == 'choice2':
                price = 150
                user_money = user_money - price

                if user_money >= 0:
                    User.objects.filter(id=user_id).update(money=user_money)
                    request.user.money = user_money

                    for i in range(0, 6):
                        cards.append(Card.objects.get(id=random.randint(1, 499)))

                    for card in cards:
                        Card_user(card_id=card.id, user_id=request.user.id).save()
                    messages.success(request, 'Vous avez acheter le pack conquérant')
                    return render(request, 'shopping/index.html')
                else:
                    messages.error(request, 'Vous n\'avez pas assez d\'argent.')
                    return render(request, 'shopping/index.html')
            elif choice == 'choice3':
                price = 300
                user_money = user_money - price

            if user_money >= 0:
                User.objects.filter(id=user_id).update(money=user_money)
                request.user.money = user_money

                for i in range(0, 12):
                    cards.append(Card.objects.get(id=random.randint(1, 499)))

                for card in cards:
                    Card_user(card_id=card.id, user_id=request.user.id).save()
                messages.success(request, 'Vous avez acheter le pack invincible')
                return render(request, 'shopping/index.html')
            else:
                messages.error(request, 'Vous n\'avez pas assez d\'argent.')
                return render(request, 'shopping/index.html')
