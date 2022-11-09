from django.urls import path
from .views import EquipmentView, EquipmentDetailView

urlpatterns = [
    path('', EquipmentView.as_view()),
    path('<pk>/', EquipmentDetailView.as_view())
]