from rest_framework import serializers
from .models import Skill

class Skill_Serializer(serializers.ModelSerializer):
    # characters = character_serializer(read_only = True)

    class Meta:
        model = Skill
        fields = '__all__'