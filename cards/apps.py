from django.apps import AppConfig
import requests
import json

from cards.models import Type_Card


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
    param_required = ('name', 'health', 'attack', 'cost', 'text', 'img', 'rarity')
    rarity_array = {1: 'Free', 2: 'Common', 3: 'Rare', 4: 'Epic', 5: 'Legendary'}

    def api_param_validator(self, card):
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

    def setup_type_cards(self):
        for key, value in self.rarity_array.items():
            s = Type_Card(key, name=value)
            s.save()

    def check_type_card(self, rarity_card):
        valid = False

        while not valid:
            for key, value in self.rarity_array.items():
                if rarity_card == value:
                    return key
                else:
                    valid = False
