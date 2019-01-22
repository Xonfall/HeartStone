from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardForm.index),
    path('all', views.CardForm.all),
    path('my_cards', views.my_cards, name="my_cards")
]