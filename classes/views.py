from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from classes.serializer import ClassSerializer
from classes.models import Class
from equipments.permissions import IsSuperUserOrReadOnly


class ClassView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_url_kwarg = "pk"
