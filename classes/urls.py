from django.urls import path

from classes.views import ClassView, ClassDetailView

urlpatterns = [
    path("", ClassView.as_view()),
    path("<pk>/", ClassDetailView.as_view()),
]
