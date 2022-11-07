from django.urls import path
from . import views

urlpatterns = [
    path('', views.CharactersView.as_view()),
    path('<str:character_id>/', views.SpecificCharacter.as_view())
]