from django.urls import path

from classes.views import ClassView, ClassDetailView

urlpatterns = [
    path("classes/", ClassView.as_view()),
    path("classes/<pk>/", ClassDetailView.as_view()),
]
