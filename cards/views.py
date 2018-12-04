from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.apps import Cards
from cards.apps import CardValidator
from cards.models import Cards
from cards.models import Rarity_cards
from cards.models import Race_cards


class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def all(request):
        cards_api = Cards()
        card_validator = CardValidator()
        all_cards = cards_api.get_all_cards()

        for cat in all_cards:
            for card in all_cards[cat]:
                if card_validator.api_param_validator(card) is True:
                    #rarity_card_model = Rarity_card(card_validator.check_type_card(card.get('rarity')))
                    #race_card_model = Race_card(card_validator.check_type_card(card.get('race')))
                    card_rarity_all = Rarity_cards.objects.all()
                    card_race_all = Race_cards.objects.all()

                    if card_rarity_all.count() == 0 and card_race_all.count() == 0:
                        for key, value in card_rarity_all:
                            print(key, value)

                    card_model = Cards.objects.create(
                        name=card['name'],
                        description=card['text'],
                        attack=card['attack'],
                        health=card['health'],
                        cost=card['cost'],
                        img=card['img'],
                     #   rarity_card=rarity_card_model,
                      #  race_card=race_card_model
                    )
                    card_model.save()

        return render(request, 'cards.html', {'lines': Cards.objects.all().count()})


def cards(request, id_card):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        card = Cards.objects.get(id=id_card)
        return render(request, 'cards.html', {'card': card})
