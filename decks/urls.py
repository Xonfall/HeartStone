from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.deck_create),
    path('ajax_deck', views.ajax_deck),
    path('ajax_addCardUser/<int:id>', views.ajax_addCardUser),
    path('ajax_addCardDeck/<int:id>', views.ajax_addCardDeck),
    path('ajax_edit/<int:id>', views.ajax_edit),
    path('ajax_createDeck', views.ajax_createDeck),
    path('ajax_editDeck/<int:id>', views.ajax_editDeck),
    path('view/<int:id>', views.view),
    path('edit/<int:id>', views.edit),
]