from django.urls import path
from .views import SkillsViews,SkillsViewsbyId

urlpatterns = [
    path('get/', SkillsViews.as_view()),
    path('get/<pk>/', SkillsViewsbyId.as_view()),
]
