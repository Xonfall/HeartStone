from django.apps import AppConfig
from collections import namedtuple
import requests
import json


class CardsConfig(AppConfig):
    name = 'cards'


class Cards:
    api_url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards'
    payload = {'locale': 'frFR'}
    headers = {'X-Mashape-Key': 'oI5kQBBnbFmsh1HykxSp39sqDBJap16s5ImjsnGbHoDtbprkGM'}

    def get_all_cards(self):
        all_cards = requests.get(self.api_url, headers=self.headers).text
        return json.loads(all_cards)

    def json_to_object(self, el):
        # Parse JSON into an object with attributes corresponding to dict keys.
        obj = json.loads(el, object_hook=lambda d: namedtuple('Cards', d.keys(), rename=True)(*d.values()))

        return obj