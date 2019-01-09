from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.shortcuts import render, redirect

from cards.apps import CardValidator
from cards.apps import Cards
from cards.models import Card
from cards.models import Race_card
from cards.models import Rarity_card
from user.models import User


class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def all(request):
        cards_api = Cards()
        card_validator = CardValidator()
        all_cards = cards_api.get_all_cards()
        card_validator.init_rarity_card_database()

        for cat in all_cards:
            for card in all_cards[cat]:
                if card_validator.check_params(card):
                    rarity_card_model = Rarity_card(card_validator.check_type_card(card.get('rarity')))
                    race_cards = Race_card.objects.all()

                    if race_cards.count() == 0:
                        race_card_model = Race_card(name=card.get('race'))
                        race_card_model.save()
                    else:
                        race_card_model = Race_card.objects.all().filter(name=card.get('race'))
                        if race_card_model.exists():
                            if str(race_card_model[0].name) != str(card.get('race')):
                                race_card_model = Race_card(name=card.get('race'))
                                race_card_model.save()
                            else:
                                race_card_model = Race_card.objects.get(name=card.get('race'))
                        else:
                            race_card_model = Race_card(name=card.get('race'))
                            race_card_model.save()

                    card_model = Card.objects.create(
                        name=card['name'],
                        description=card['text'],
                        attack=card['attack'],
                        health=card['health'],
                        cost=card['cost'],
                        img=card['img'],
                        rarity_card=rarity_card_model,
                        race_card=race_card_model
                    )
                    card_model.save()

        return render(request, 'cards.html', {'lines': Card.objects.all().count()})


def cards(request, id_card):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        card = Card.objects.get(id=id_card)
        return render(request, 'cards.html', {'card': card})


@login_required
def my_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        u1 = request.user
        get_cards = u1.card_set.all()

    return render(request, 'my_cards.html', {'all_cards': get_cards})
