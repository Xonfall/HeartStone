from django.contrib.auth.decorators import login_required
from django.db.models import Count

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
    return render(request, 'view.html', {'deck_name': deck, 'deck_cards': relative_news})


@login_required
def deck_create(request):
    if request.POST:
        form = DecksForm(request.POST)
    else:
        form = DecksForm()
    return render(request, 'create.html', {'form': form})


@login_required
def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        deck = get_object_or_404(Deck, id=id)
        form = DecksForm(request.POST or None, instance=deck)
        relative_news = Card.objects.filter(deck_user__in=Deck_user.objects.filter(deck_id=id))
        return render(request, "edit.html", {'form': form})


def deck_create(request):
    if request.POST:
        form = DecksForm(request.POST)
    else:
        form = DecksForm()
    return render(request, 'create.html', {'form': form})


@login_required
def ajax_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        result_decks = dict()
        response_data = []

        for e in Deck_user.objects.filter(deck_id=id).order_by('card_id'):
            for u in Card.objects.filter(id=e.card_id):
                list_of_cards = {'id_user_card': e.id, 'id': u.id, 'name': u.name, 'img': u.img}
                response_data.append(list_of_cards)

        result_decks['data'] = response_data
        return HttpResponse(
            json.dumps(result_decks),
            content_type="application/json"
        )


@login_required
def ajax_deck(request):
    result_decks = dict()
    response_data = []

    for e in Card_user.objects.filter(user_id=request.user.id).order_by('card_id'):
        for u in Card.objects.filter(id=e.card_id):
            list_of_cards = {'id_user_card': e.id, 'id': u.id, 'name': u.name, 'img': u.img}
            response_data.append(list_of_cards)

    result_decks['data'] = response_data
    return HttpResponse(
        json.dumps(result_decks),
        content_type="application/json"

    )


@login_required
def ajax_createDeck(request):
    if request.is_ajax():
        get_all_cards = request.POST['cards[]']
        name = request.POST['name']
        deck1 = Deck()
        deck1.name = name
        deck1.user = request.user
        deck1.save()
        arrayGetcountDoublon = []
        for i in json.loads(get_all_cards):
            entry = Deck.objects.get(id=deck1.id)
            insert_cards = Deck_user(card_id=i['card_id'], deck_id=entry.id)
            insert_cards.save()
            arrayGetcountDoublon.append(i['card_id'])

        count_cards = {k: arrayGetcountDoublon.count(k) for k in set(arrayGetcountDoublon)}

        for i in count_cards:
            if i:

                cccmoi = list(Card_user.objects.filter(card_id=i))
                for zizi in range(count_cards[i]):
                    Card_user.objects.filter(user_id=request.user.id, id=cccmoi[zizi].id).delete()

    return HttpResponse('ok')


@login_required
def ajax_addCardUser(request, id):
    if request.is_ajax():
        addCardsId = request.POST['addCardsId']
        insertUserCards = Card_user(card_id=addCardsId, user_id=request.user.id)
        insertUserCards.save()
        cccmoi = list(Deck_user.objects.filter(card_id=addCardsId)[:1])
        for i in cccmoi:
            Deck_user(id=i.id, deck_id=id).delete()

    return HttpResponse('ok')


@login_required
def ajax_addCardDeck(request, id):
    if request.is_ajax():
        addCardsDeckId = request.POST['addCardsDeckId']
        insertDeckCards = Deck_user(card_id=addCardsDeckId, deck_id=id)
        insertDeckCards.save()
        cccmoi = list(Card_user.objects.filter(card_id=addCardsDeckId)[:1])
        for i in cccmoi:
            Card_user(id=i.id, user_id=request.user.id).delete()

    return HttpResponse('ok')


@login_required
def ajax_editDeck(request, id):
    if request.is_ajax():

        getAllCards = request.POST['cards[]']
        name = request.POST['name']
        Deck.objects.filter(id=id).update(name=name)
        arrayGetcountDoublon = []

        Deck_user.objects.filter(deck_id=id).delete();

        for i in json.loads(getAllCards):
            entry = Deck.objects.get(id=id)
            inserCards = Deck_user(card_id=i['card_id'], deck_id=entry.id)
            inserCards.save()
            arrayGetcountDoublon.append(i['card_id'])

        count_cards = {k: arrayGetcountDoublon.count(k) for k in set(arrayGetcountDoublon)}

        for i in count_cards:
            if i:
                cccmoi = list(Card_user.objects.filter(card_id=i))
                for zizi in range(count_cards[i]):
                    Card_user.objects.filter(user_id=request.user.id, id=cccmoi[zizi].id).delete()

    return HttpResponse('ok')
