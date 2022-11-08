from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .models import Skill
from .serializers import Skill_Serializer
from equipments.permissions import IsSuperUserOrReadOnly


class SkillView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsSuperUserOrReadOnly]

    queryset = Skill.objects.all()
    serializer_class = Skill_Serializer