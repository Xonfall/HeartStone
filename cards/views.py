from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.apps import Cards
from cards.models import Card


class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def example(request):
        cards = Cards()
        db = Card()

        all_cards = cards.get_all_cards()

        if all_cards.img is not None:
            db.save(name=)

        return render(request, 'cards.html', {'cards': all_cards})
