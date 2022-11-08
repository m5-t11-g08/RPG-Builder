from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from classes.serializer import ClassSerializer
from classes.models import Class
from classes.permissions import IsSuperUser


class ClassView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsSuperUser]

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsSuperUser]

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_url_kwarg = "pk"
