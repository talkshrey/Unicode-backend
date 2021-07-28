from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.pokFetcher, name='pokedex'),
  # path('', views.typeFetcher, name='type'),
  # path('', views.form, name='choice'),
]
