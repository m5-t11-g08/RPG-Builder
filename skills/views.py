from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import generics

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

from .models import Skill
from .serializers import Skill_Serializer

class SkillsViews(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

class SkillsViewsbyId(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer

