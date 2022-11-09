from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .permissions import IsSuperUserOrReadOnly
from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
