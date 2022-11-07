from django.urls import path
from .views import SkillsGetViews,SkillsViewsbyId,SkillsCreateViews,SkillsGetViewsbyId

urlpatterns = [
    path('', SkillsGetViews.as_view()),
    path('get/<pk>/', SkillsGetViewsbyId.as_view()),
    path('create/', SkillsCreateViews.as_view()),
    path('<pk>/', SkillsViewsbyId.as_view()),
]
