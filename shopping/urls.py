from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('buy', views.buy_cards, name='buy_cards'),
]


