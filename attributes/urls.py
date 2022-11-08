from django.urls import path
from . import views

urlpatterns = [
    path("<int:character_id>/", views.AttributesRetrieveCharacter.as_view()),
    path("", views.GetAttributes.as_view()),
]