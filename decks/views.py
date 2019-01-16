from django.contrib.auth.decorators import login_required

from cards.models import Card_user
from decks.models import Deck_user
from decks.models import Deck
from decks.models import Card
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DecksForm
import json
from django.core import serializers
import collections


@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:

        getDecks = Deck.objects.filter(user_id=request.user)

        return render(request, 'index.html', {'getDecks': getDecks})


def view(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        deck = Deck.objects.get(id=id)

        relative_news = Card.objects.filter(deck_user__in=Deck_user.objects.filter(deck_id=id))

        print(relative_news)

    return render(request, 'view.html', {'deck_name': deck, 'deck_cards': relative_news})


@login_required
def deck_create(request):
    if request.POST:
        form = DecksForm(request.POST)
    else:
        form = DecksForm()

        # form.fields["user"].initial = [request.user.id]

    return render(request, 'create.html', {'form': form})


@login_required
def ajax_deck(request):
    result_decks = dict()
    response_data = []
    relative_news = list(Card.objects.filter(deck_user__in=Deck_user.objects.filter(deck_id=12)))

    d = {x: relative_news.count(x) for x in relative_news}
    print(d)

    for u in Card.objects.filter(card_user__in=Card_user.objects.filter(user_id=request.user.id).exclude(
            card__deck_user__deck__in=Deck.objects.filter(user_id=request.user.id))):


        list_of_cards = {'id': u.id, 'name': u.name, 'img': u.img}
        response_data.append(list_of_cards)

    result_decks['data'] = response_data

    return HttpResponse(
        json.dumps(result_decks),
        content_type="application/json"

    )


@login_required
def ajax_createDeck(request):
    if request.is_ajax():
        user = request.user
        get_all_cards = request.POST['cards[]']
        name = request.POST['name']
        deck1 = Deck()
        deck1.name = name
        deck1.user = request.user
        deck1.save()

        for i in json.loads(get_all_cards):
            print(i['card_id'])
            entry = Deck.objects.get(id=deck1.id)
            insert_cards = Deck_user(card_id=i['card_id'], deck_id=entry.id)
            insert_cards.save()

    return HttpResponse('ok')
