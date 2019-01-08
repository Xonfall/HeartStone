from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardForm.index),
    path('all', views.CardForm.all)
]