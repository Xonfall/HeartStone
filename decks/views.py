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

        form.fields["user"].initial = [request.user.id]

    return render(request, 'index.html', {'form': form})


def ajax_deck(request):
    result_decks = dict()
    response_data = []

    for u in request.user.card_set.all():
        list_of_cards = {'id': u.id, 'name': u.name, 'img': u.img}
        response_data.append(list_of_cards)

    result_decks['data'] = response_data

    return HttpResponse(
        json.dumps(result_decks),
        content_type="application/json"

    )
