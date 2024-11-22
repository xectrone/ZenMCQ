from django.urls import path
from .views import create_deck_view, add_mcq_view, deck_detail_view, all_decks_view

urlpatterns = [
    path('deck/create/', create_deck_view, name='create_deck'),
    path('deck/<uuid:deck_id>/mcq/add/', add_mcq_view, name='add_mcq'),
    path('deck/<uuid:deck_id>/', deck_detail_view, name='deck_detail'),
     path('decks/', all_decks_view, name='all_decks'),
]
