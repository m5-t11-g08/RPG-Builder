from django.urls import path
from .views import SkillView, SkillDetailView

urlpatterns = [
    path('', SkillView.as_view()),
    path("<pk>/", SkillDetailView.as_view())
]