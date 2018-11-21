from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.apps import Cards
from cards.apps import CardValidator
from cards.models import Card
from cards.models import Type_Card


class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def all(request):
        cards_api = Cards()
        card_validator = CardValidator()
        all_cards = cards_api.get_all_cards()

        # Enregistre les données Type_card en BDD
        if Type_Card.objects.all().count() == 0:
            card_validator.setup_type_cards()

        for cat in all_cards:
            for card in all_cards[cat]:
                if card_validator.api_param_validator(card) is True:
                    type_card_model = Type_Card(card_validator.check_type_card(card.get('rarity')))
                    card_model = Card.objects.create(
                        name=card['name'],
                        description=card['text'],
                        attack=card['attack'],
                        health=card['health'],
                        cost=card['cost'],
                        img=card['img'],
                        type_card=type_card_model
                    )
                    card_model.save()

        return render(request, 'cards.html', {'lines': Card.objects.all().count()})


def cards(request, id_card):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        card = Card.objects.get(id=id_card)
        return render(request, 'cards.html', {'card': card})
