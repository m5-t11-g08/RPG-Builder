from rest_framework import serializers
from .models import Skill

class Skill_Serializer(serializers.ModelSerializer):
    # characters = character_serializer(read_only = True)

    class Meta:
        model = Skill
        fields = [
            'id',
            'name',
            'damage',
            'mana_cost',
        ]

        # extra_kwargs = {'id': {'read_only': True}}

    # def create(self, validated_data:dict) -> Skill:
    #     new_skill = Skill.objects.create(**validated_data)
    #     return new_skill
