from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from exchange.models import Buy
from exchange.models import Exchange
from user.models import User
from django.http import HttpResponse
from cards.models import Card, Card_user


# Create your views here.

def index(request):
    cards = Exchange.objects.raw(
        "select exchange_exchange.id, cc.name, cc.img, uu.username, crc.name, created_at from exchange_exchange join cards_card cc on exchange_exchange.card_receiver_id = cc.id join user_user uu on exchange_exchange.user_id = uu.id join cards_rarity_card crc on cc.rarity_card_id = crc.id where exchange_statut = 'pending'")

    return render(request, 'exchange/index.html', {"cards": cards})


@login_required
def new(request):
    if request.method == 'GET':
        if Card.objects.filter(card_user__in=Card_user.objects.filter(user_id=request.user.id)).count() == 0:
            return render(request, 'exchange/add.html', {'message': 'Vous n\'avez pas de carte a échanger'})
        else:
            return render(request, 'exchange/add.html',
                          {
                              'own_cards': Card.objects.filter(
                                  card_user__in=Card_user.objects.filter(user_id=request.user.id)).order_by('name'),
                              'all_cards': Card.objects.all()
                          })
    if request.method == 'POST':
        title = request.POST['title']
        id_card_sender = request.POST['cards']
        id_card_receiver = request.POST['card_demand']

        query = Exchange(exchange_statut="pending", user_id=request.user.id, title=title,
                         card_sender=Card(id=id_card_sender), card_receiver=Card(id=id_card_receiver)).save()

        return render(request, 'exchange/index.html', {'message': 'Votre demande a été enregistré'})
