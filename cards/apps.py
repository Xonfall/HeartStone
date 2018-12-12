from django.apps import AppConfig
from cards.models import Race_card
from cards.models import Card
from cards.models import Rarity_card

import requests
import json

from cards.models import Rarity_cards


class CardsConfig(AppConfig):
    name = 'cards'


class Cards:
    api_url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards'
    payload = {'locale': 'frFR'}
    headers = {'X-Mashape-Key': 'oI5kQBBnbFmsh1HykxSp39sqDBJap16s5ImjsnGbHoDtbprkGM'}

    def get_all_cards(self):
        all_cards = requests.get(self.api_url, headers=self.headers, params=self.payload).text
        return json.loads(all_cards)


class CardValidator:
    param_required = ('name', 'health', 'attack', 'cost', 'text', 'img', 'rarity', 'race')
    rarity_array = {1: 'Free', 2: 'Common', 3: 'Rare', 4: 'Epic', 5: 'Legendary'}

    def check_params(self, card):
        valid = []
        lenght_params = len(self.param_required)
        count = 0

        for param in self.param_required:
            if card.get(param) is not None:
                valid.append(True)
            else:
                valid.append(False)

        for value in valid:
            if value is True:
                count += 1
                if count == lenght_params:
                    return True
            else:
                return False

    def init_rarity_card_database(self):
        for key, value in self.rarity_array.items():
            s = Rarity_card(key, name=value)
            s.save()

    def init_race_card_database(self, race_name):
        get_race = Race_card.objects.all().filter(name=race_name)

        if get_race is not None:
            return True
        else:
            race = Race_card(name=race_name)
            race.save()

    def check_type_card(self, card):
        valid = False

        while not valid:
            for key, value in self.rarity_array.items():
                if card == value:
                    return key
                else:
                    valid = False
