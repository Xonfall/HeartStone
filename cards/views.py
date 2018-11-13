from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cards.apps import Cards
from cards.models import Card
from cards.models import Type_Card


class CardForm(ModelForm):

    # @login_required
    def index(request):
        return render(request, 'index.html')

    def example(request):
        cards = Cards()
        all_cards = cards.get_all_cards()

        tab = ('Classic',
               'Promo',
               'Hall of Fame',
               'Naxxramas', 'Goblins vs Gnomes', 'Blackrock Mountain', 'The Grand Tournament',
               'The League of Explorers', 'Whispers of the Old Gods', 'One Night in Karazhan',
               'Mean Streets of Gadgetzan', 'Journey to Un\'Goro', 'Knights of the Frozen Throne',
               'Kobolds & Catacombs', 'The Witchwood', 'The Boomsday Project', 'Tavern Brawl')
        for dlc in tab:
            for card in all_cards[dlc]:
                if card.get('img') is not None and \
                        card.get('text') is not None and \
                        (card.get('race') == 'Beast' or \
                         card.get('race') == 'Murloc' or
                         card.get('race') == 'Pirate' or
                         card.get('race') == 'Elemental') and \
                        card.get('rarity') is not None:
                    if card.get('rarity') == 'Common':
                        type_card = Type_Card(1)
                    elif card.get('rarity') == 'Rare':
                        type_card = Type_Card(2)
                    elif card.get('rarity') == 'Epic':
                        type_card = Type_Card(3)
                    elif card.get('rarity') == 'Legendary':
                        type_card = Type_Card(4)
                    else:
                        type_card = Type_Card(0)
                    card = Card(name=card['name'],
                                description=card['text'],
                                type_card_id=type_card,
                                attack=card['attack'],
                                img=card['img'])
                    card.save()

        return render(request, 'cards.html', {'cards': all_cards})

    def cards(request, id_card):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            card = Card.objects.get(id=id_card)
            return render(request, 'cards.html', {'card': card})
