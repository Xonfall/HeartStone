from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.deck_create),
    path('ajax_deck', views.ajax_deck),
    path('ajax_createDeck', views.ajax_createDeck),
    path('view/<int:id>', views.view),
]