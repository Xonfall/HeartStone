from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.apps import Cards

class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def example(request):
        cards = Cards()
        all_cards = cards.get_all_cards()

        return render(request, 'cards.html', {'cards': all_cards})
