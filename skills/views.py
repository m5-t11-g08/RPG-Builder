from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .permissions import So_adm
from rest_framework.authentication import TokenAuthentication

from .models import Skill
from .serializers import Skill_Serializer

class SkillsGetViews(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

class SkillsCreateViews(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [So_adm]
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

class SkillsViewsbyId(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [So_adm]
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

class SkillsGetViewsbyId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

