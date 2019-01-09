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

                    for i in range(0, 4):
                        cards.append(Card.objects.get(id=random.randint(1, 499)))

                    for card in cards:
                        Card(id=card.id).users.add(User(id=user_id))

                    return render(request, 'shopping/index.html')
                else:
                    return render(request, 'shopping/index.html')
            elif choice == 'choice2':
                price = 150
                user_money = user_money - price

                if user_money >= 0:
                    User.objects.filter(id=user_id).update(money=user_money)

                    for i in range(0, 6):
                        cards.append(Card.objects.get(id=random.randint(1, 499)))

                    for card in cards:
                        Card(id=card.id).users.add(User(id=user_id))

                    return render(request, 'shopping/index.html')
                else:
                    return render(request, 'shopping/index.html')
            elif choice == 'choice3':
                price = 300
                user_money = user_money - price

            if user_money >= 0:
                User.objects.filter(id=user_id).update(money=user_money)

                for i in range(0, 12):
                    cards.append(Card.objects.get(id=random.randint(1, 499)))

                for card in cards:
                    Card(id=card.id).users.add(User(id=user_id))

                return render(request, 'shopping/index.html')
            else:
                return render(request, 'shopping/index.html')
