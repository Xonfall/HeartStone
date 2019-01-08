from deck.models import Deck
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['name', "user", "cards"]


def show_deck(request, id_deck):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        deck = Deck.objects.get(id=id_deck)
        return render(request, 'decks.html', {'deck': deck})


def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'listdecks.html', {'decks': decks})


def deck_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.POST:
            form = DeckForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listdecks')
        else:
            # form = DeckForm()
            form = DeckForm()
            form.fields["user"].initial = [request.user.id]
            form.fields["cards"].queryset = request.user.card_set.all()
        return render(request, 'createdeck.html', {'form': form})


def deck_update(request, id_deck):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        deck = get_object_or_404(Deck, id=id_deck)
        form = DeckForm(request.POST or None, instance=deck)
        if form.is_valid():
            form.save()
            return redirect('deck_list')
        return render(request, "decks.html", {'form': form})


def deck_delete(request, id_deck):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        deck = Deck.objects.get(id=id_deck)
        deck.delete()
        return redirect('listdecks')
