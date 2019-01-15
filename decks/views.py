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


def deck_create(request):
    if request.POST:
        form = DecksForm(request.POST)
    else:
        form = DecksForm()

        #form.fields["user"].initial = [request.user.id]

    return render(request, 'index.html', {'form': form})


def ajax_deck(request):
    result_decks = dict()
    response_data = []

    for u in Card.objects.filter(card_user__in=Card_user.objects.filter(user_id=request.user.id)):
        list_of_cards = {'id': u.id, 'name': u.name, 'img': u.img}
        response_data.append(list_of_cards)

    result_decks['data'] = response_data

    return HttpResponse(
        json.dumps(result_decks),
        content_type="application/json"

    )


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
