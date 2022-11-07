from django.urls import path
from .views import (
    EquipmentGetViews,
    EquipmentCreateViews,
    EquipmentViewsById,
    EquipmentGetViewsById,
)

urlpatterns = [
    path("", EquipmentGetViews.as_view()),
    path("get/<pk>/", EquipmentViewsById.as_view()),
    path("create/", EquipmentCreateViews.as_view()),
    path("<pk>/", EquipmentGetViewsById.as_view()),
]
