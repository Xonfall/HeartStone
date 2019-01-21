from decks.models import Deck
from django.forms import ModelForm


class DecksForm(ModelForm):
    class Meta:
        model = Deck
        fields = {'name'}
