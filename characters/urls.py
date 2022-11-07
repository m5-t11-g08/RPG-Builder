from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.CharactersView.as_view()),
    path('characters/<int:character_id>/', views.SpecificCharacter.as_view())
]