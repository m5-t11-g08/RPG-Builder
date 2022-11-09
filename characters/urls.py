from django.urls import path
from .views import CharactersView, SpecificCharacter

urlpatterns = [
    path('', CharactersView.as_view()),
    path('<str:character_id>/', SpecificCharacter.as_view())
]