from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdm

from .models import Equipment
from .serializers import EquipmentSerializer


class EquipmentGetViews(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentCreateViews(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdm]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentGetViewsById(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentViewsById(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdm]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
