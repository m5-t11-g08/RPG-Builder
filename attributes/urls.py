from django.urls import path
from . import views

urlpatterns = [
    path("<str:character_id>/", views.AttributesRetrieveCharacter.as_view()),
    path("", views.GetAttributes.as_view()),
]