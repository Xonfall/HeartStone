
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CardForm.index),
    path('all', views.CardForm.all)
]